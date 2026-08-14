books = []

def show_menu():
    print('''
    ==================================
                BOOK MANAGER
    ==================================
    1. Добавить книгу
    2. Показать все книги
    3. Найти книгу
    4. Удалить книгу
    5. Статистика
    6. Изменить книгу
    0. Выход
    ''')

def add_book():
    pass

def show_books():
    pass

def find_book():
    pass

def delete_book():
    pass

def show_statistics():
    pass

def edit_book():
    pass

def main():
    while True:
        show_menu()
        choice = input("Выберите действие: ")

        if choice == "1":
            add_book()
        elif choice == "2":
            show_books()
        elif choice == "3":
            find_book()
        elif choice == "4":
            delete_book()
        elif choice == "5":
            show_statistics()
        elif choice == "6":
            edit_book()
        elif choice == "0":
            print("Программа завершена.")
            break
        else:
            print("Неверный пункт меню.")


main()