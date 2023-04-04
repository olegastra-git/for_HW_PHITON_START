# Создаем пустой телефонный справочник
phonebook = {}
print("\nСписок контактов:")
# Функция для добавления контакта в телефонный справочник
def add_contact():
    name = input("Введите имя контакта: ")
    number = input("Введите номер контакта: ")
    if name not in phonebook:
        phonebook[name] = number
        print("Контакт успешно добавлен")
    else:
        print("Контакт уже существует")

# Функция для изменения номера контакта в телефонном справочнике
def edit_contact():
    name = input("Введите имя контакта, который необходимо изменить: ")
    if name in phonebook:
        new_number = input("Введите новый номер контакта: ")
        phonebook[name] = new_number
        print("Контакт успешно изменен")
    else:
        print("Контакт не найден")

# Функция для удаления контакта из телефонного справочника
def delete_contact():
    name = input("Введите имя контакта, который необходимо удалить: ")
    if name in phonebook:
        del phonebook[name]
        print("Контакт успешно удален")
    else:
        print("Контакт не найден")

# Функция для поиска контакта в телефонном справочнике
def search_contact():
    name = input("Введите имя контакта для поиска: ")
    if name in phonebook:
        print(f"Номер контакта {name}: {phonebook[name]}")
    else:
        print("Контакт не найден")

# Меню функций
menu = {
    "1": add_contact,
    "2": edit_contact,
    "3": delete_contact,
    "4": search_contact
}

# Выводим приглашение для выбора команды
print("Телефонный справочник\n------------------------")
print("Выберите действие:")
print("1. Добавить контакт")
print("2. Изменить контакт")
print("3. Удалить контакт")
print("4. Найти контакт")

# Запускаем бесконечный цикл для работы с телефонным справочником
while True:
    choice = input("\nВыберите команду (или q для выхода): ")
    if choice == "q":
        break
    elif choice in menu:
        menu[choice]()
    else:
        print("Неверная команда")

# Проверяем добавление контакта Иван с номером 789654
phonebook["Иван"] = "789654"

# Выводим окончательный список контактов
print("\nСписок контактов:")
for name, number in phonebook.items():
    print(f"{name}: {number}")
