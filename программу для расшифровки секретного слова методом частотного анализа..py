# Ввод зашифрованного слова
encrypted_word = input("Введите зашифрованное слово: ")

# Создаем словарь для хранения частот
letter_frequency = {}

# Разбиваем зашифрованное слово на буквы и подсчитываем частоту каждой буквы
for letter in encrypted_word:
    if letter in letter_frequency:
        letter_frequency[letter] += 1
    else:
        letter_frequency[letter] = 1

# Ввод количества итераций
n = int(input("Введите количество итераций: "))

# Создаем словарь для хранения частот букв из словаря
dictionary_frequency = {}

# Считываем частоты букв из словаря
for _ in range(n):
    input_str = input("Введите букву и частоту в формате 'a:2': ")
    parts = input_str.split(":")
    if len(parts) == 2:
        letter = parts[0].strip()
        frequency = int(parts[1])
        dictionary_frequency[letter] = frequency

# Инициализируем пустой словарь для хранения замен
replacements = {}

# Проходим по буквам словаря и заменяем их на буквы из зашифрованного слова
for letter in dictionary_frequency.keys():
    for encrypted_letter, frequency in letter_frequency.items():
        if frequency == dictionary_frequency[letter]:
            replacements[encrypted_letter] = letter
            letter_frequency[encrypted_letter] = 0
            break

# Проходим по всем заменам и заменяем буквы в зашифрованном слове
decrypted_word = ""
for letter in encrypted_word:
    if letter in replacements:
        decrypted_word += replacements[letter]
    else:
        decrypted_word += letter

print(f"Расшифрованное слово: {decrypted_word}")


