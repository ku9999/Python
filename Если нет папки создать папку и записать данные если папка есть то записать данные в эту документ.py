import os

desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
document_name = input("Введите название документа: ")
document_path = os.path.join(desktop_path, document_name)

data = input("Введите данные для записи: ")

with open(document_path, 'a') as file:
    file.write(data)
