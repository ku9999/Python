import time
import requests
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import csv
import os
from datetime import datetime
from google_play_scraper import app, search

# === НАСТРОЙКИ ===

GOOGLE_SHEETS_KEY = "1ERmKj9Y6ZG7VCnpRN1e4Sl66ruz4kf69hLTA53YcHcY"
CREDENTIALS_FILE = "credentials.json"

BULKEMAILCHECKER_API_KEY = "qtwW05DdxKNSkrJhyjPQTY7faAIsVEBu"
MAX_APPS = 133  # Сколько **валидных** игровых записей нужно добавить за запуск

# === ИНИЦИАЛИЗАЦИЯ GOOGLE SHEETS ===

scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE, scope)
client = gspread.authorize(creds)
sheet = client.open_by_key(GOOGLE_SHEETS_KEY).sheet1

# Заголовки таблицы (если первый запуск; иначе закомментируйте)
headers = [
    "ID приложения",
    "Название",
    "Скачивания",
    "Email разработчика",
    "Разработчик",
    "Страна",
    "Рейтинг",
    "Дата выхода",
    "Подкатегория",
    "Наличие видео"
]
try:
    sheet.update(range_name="A1:J1", values=[headers])
except Exception as e:
    print(f"⚠️ Не удалось обновить заголовки в Google Sheets: {e}")

# Считываем уже существующие email, чтобы не добавлять дубликаты
try:
    existing_emails = set(email for email in sheet.col_values(4)[1:] if email)
except Exception:
    existing_emails = set()

# === ФУНКЦИИ ===

def validate_email(email: str) -> bool:
    """
    Проверка email через BulkEmailChecker API.
    - Если status_code=200, возвращает True только если status=="passed".
    - Если status_code=403, выводит предупреждение и возвращает True (считаем валидным).
    - В остальных случаях возвращает False.
    """
    if not email:
        return False
    url = f"https://api.bulkemailchecker.com/?key={BULKEMAILCHECKER_API_KEY}&email={email}"
    try:
        response = requests.get(url, timeout=10)
    except requests.RequestException as e:
        print(f"❗ Ошибка запроса к BulkEmailChecker: {e}")
        return False

    if response.status_code == 200:
        try:
            data = response.json()
        except ValueError:
            print("❗ Не удалось распарсить JSON от BulkEmailChecker")
            return False
        return data.get("status") == "passed"
    elif response.status_code == 403:
        print(f"❗ BulkEmailChecker вернул 403. Пропускаем проверку для {email} (считаем валидным).")
        return True
    else:
        print(f"❗ BulkEmailChecker вернул код {response.status_code} для {email}")
        return False

def save_to_csv(row_data: list, filename_prefix="backup_export"):
    """
    Сохраняет row_data в CSV <filename_prefix>_<YYYY-MM-DD>.csv.
    Если файл новый, сначала пишет заголовки.
    """
    date_str = datetime.now().strftime("%Y-%m-%d")
    filename = f"{filename_prefix}_{date_str}.csv"
    file_exists = os.path.isfile(filename)
    try:
        with open(filename, "a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            if not file_exists:
                writer.writerow(headers)
            writer.writerow(row_data)
    except Exception as e:
        print(f"❗ Не удалось сохранить в CSV ({filename}): {e}")

# === ГЕНЕРАЦИЯ СПИСКА app_id С ПОМОЩЬЮ ПОИСКА ПО КЛЮЧЕВОМУ СЛОВУ ===

# Перебираем ключи “a”…“z” и “0”…“9” до тех пор, пока не соберём MAX_APPS валидных email именно для игр
alphabet = [chr(i) for i in range(ord("a"), ord("z") + 1)] + [str(d) for d in range(0, 10)]
collected_ids = []
added_count = 0

for keyword in alphabet:
    if added_count >= MAX_APPS:
        break
    try:
        # Поиск по ключевому слову (возвращает около 10–20 результатов без категории)
        results = search(keyword, lang="en", country="us")
    except Exception as e:
        print(f"⚠️ Ошибка поиска по ключу '{keyword}': {e}")
        continue

    for item in results:
        if added_count >= MAX_APPS:
            break
        app_id = item.get("appId")
        if not app_id or app_id in collected_ids:
            continue
        collected_ids.append(app_id)

        # Получаем детальную информацию по приложению
        try:
            data = app(app_id, lang="ru", country="ru")
        except Exception as e:
            print(f"⚠️ Ошибка при запросе данных Google Play для '{app_id}': {e}")
            continue

        # Проверяем, что это приложение из категории "Игры"
        genre_id = data.get("genreId", "")
        if not genre_id.startswith("GAME"):
            # Пропускаем любые не-игровые приложения
            continue

        title = data.get("title", "")
        installs = data.get("installs", "N/A")
        developer = data.get("developer", "")
        email = data.get("developerEmail", "")
        address_full = data.get("developerAddress", "")
        country = address_full.split(",")[-1].strip() if address_full else ""
        rating = data.get("score", "")
        released = data.get("released", "")
        subcategory = data.get("genre", "")
        has_video = bool(data.get("video"))

        # Пропуск, если нет email или email уже есть
        if not email:
            print(f"⏭ Пропуск (нет email): {app_id}")
            continue
        if email in existing_emails:
            print(f"⏭ Пропуск (дубликат email): {email}")
            continue

        # Валидация email
        if not validate_email(email):
            print(f"⛔ Email не прошёл валидацию: {email}")
            continue

        # Формируем строку для записи
        row_data = [
            app_id,
            title,
            installs,
            email,
            developer,
            country,
            rating,
            released,
            subcategory,
            "Да" if has_video else "Нет"
        ]

        # Пытаемся записать в Google Sheets
        try:
            sheet.append_row(row_data)
            print(f"✅ Добавлено в Google Sheets: {app_id}")
        except Exception as e:
            print(f"❗ Не удалось записать в Google Sheets: {e} — сохраняем в CSV.")
            save_to_csv(row_data)

        existing_emails.add(email)
        added_count += 1
        time.sleep(1)  # Задержка между запросами, чтобы не перегружать API

print(f"🎯 Сбор завершён. Добавлено {added_count} записей.")

# === ЕЖЕНЕДЕЛЬНЫЙ ЭКСПОРТ В CSV ===

# Если сегодня понедельник (weekday()==0), создаём полный экспорт Google Sheets в CSV
if datetime.today().weekday() == 0:
    try:
        all_values = sheet.get_all_values()
        week_fname = f"weekly_backup_{datetime.now().strftime('%Y-%m-%d')}.csv"
        with open(week_fname, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(all_values)
        print(f"🗂 Еженедельный CSV-экспорт выполнен: {week_fname}")
    except Exception as e:
        print(f"❗ Ошибка при еженедельном экспорте в CSV: {e}")
