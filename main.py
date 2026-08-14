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
    title = input("Введите название книги: ").strip()
    author = input("Введите автора: ").strip()
    year = input("Введите год выпуска: ").strip()

    if title == "" or author == "":
        print("Название и автор не могут быть пустыми")
        return

    if not year.isdigit():
        print("Год должен быть числом")
        return

    year = int(year)
    current_year = 2026

    if year < 1500 or current_year < year:
        print("Год должен быть от 1500 до", current_year)
        return

    exists = False
    for book in books:
        if book[0].lower() == title.lower():
            exists = True

    if exists:
        print("Книга с таким названием уже есть в библиотеке")
        return

    books.append([title, author, year])
    print("Книга успешно добавлена!")

def show_books():
    if len(books) == 0:
        print("Библиотека пустая")
        return

    number = 1
    for book in books:
        print(str(number) + ". " + book[0] + " - " + book[1] + " (" + str(book[2]) + " год.)")
        number = number + 1

def find_book():
    if len(books) == 0:
        print("Библиотека пустая")
        return

    search = input("Введите часть названия: ").strip().lower()

    found = False
    number = 1
    for book in books:
        if search in book[0].lower():
            print(str(number) + ". " + book[0] + " - " + book[1] + " (" + str(book[2]) + ")")
            found = True
        number = number + 1

    if not found:
        print("Книга не найдена")

def delete_book():
    if len(books) == 0:
        print("Библиотека пустая")
        return

    show_books()
    number = input("Введите номер книги: ").strip()

    if not number.isdigit():
        print("Неверный номер книги")
        return

    number = int(number)

    if number < 1 or number > len(books):
        print("Неверный номер книги")
        return

    book = books[number - 1]
    books.pop(number - 1)
    print("Книга " + book[0] + " удалена!")

def show_statistics():
    if len(books) == 0:
        print("Библиотека пустая")
        return

    oldest = books[0][2]
    newest = books[0][2]

    for book in books:
        if book[2] < oldest:
            oldest = book[2]
        if book[2] > newest:
            newest = book[2]

    print("Всего книг:", len(books))
    print("Самая старая книга:", oldest)
    print("Самая новая книга:", newest)

def edit_book():
    if len(books) == 0:
        print("Библиотека пустая")
        return

    show_books()
    number = input("Введите номер книги: ").strip()

    if not number.isdigit():
        print("Неверный номер книги.")
        return

    number = int(number)

    if number < 1 or number > len(books):
        print("Неверный номер книги.")
        return

    book = books[number - 1]

    title = input("Новое название (Enter - оставить " + book[0] + "): ").strip()
    author = input("Новый автор (Enter - оставить " + book[1] + "): ").strip()
    year = input("Новый год (Enter - оставить " + str(book[2]) + "): ").strip()

    if title != "":
        book[0] = title

    if author != "":
        book[1] = author

    if year != "":
        if not year.isdigit():
            print("Год должен быть числом, год не изменён.")
        else:
            year = int(year)
            current_year = 2026
            if year < 1500 or current_year < year:
                print("Год должен быть от 1500 до", current_year, "- год не изменён.")
            else:
                book[2] = year

    print("Книга изменена.")



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
            print("Book manager остановлен спасибо что воспользовались нашим библиотекой.")
            break
        else:
            print("Вы ввели не существующего меню")


main()