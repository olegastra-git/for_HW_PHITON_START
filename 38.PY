# Телефонный справочник на Python
# Создаем пустой словарь для хранения контактов
phonebook = {}
# Функция добавления контакта
def add_contact():
     name = input("Введите имя контакта: ")
     number = input("Введите номер телефона контакта: ")
     phonebook[name] = number
     print("Контакт добавлен!")
# Функция изменения контакта
def change_contact():
      name = input("Введите имя контакта, который нужно изменить: ")
if name in phonebook:
      number = input("Введите новый номер телефона контакта: ")
      phonebook[name] = number
      print("Контакт изменен!")
else:
      print("Контакт не найден.")
# Функция удаления контакта
def delete_contact():
    name = input("Введите имя контакта, который нужно удалить: ")
if name in phonebook:
    del phonebook[name]
    print("Контакт удален!")
else:
    print("Контакт не найден.")
# Основной цикл программы
while True:
    print("\nТелефонный справочник:")
    print("1. Добавить контакт")
    print("2. Изменить контакт")
    print("3. Удалить контакт")
    print("4. Показать все контакты")
    print("5. Выход")
choice = int(input("Выберите действие: "))
if choice == 1:
    add_contact()
elif choice == 2:
    change_contact()
elif choice == 3:
    delete_contact()
elif choice == 4:
    print("Список всех контактов:")
for name, number in phonebook.items():
    print(name + ": " + number)
elif choice == 5:
    print("Выход из программы...")
break

else:
    print("Неверный выбор. Попробуйте еще раз."
