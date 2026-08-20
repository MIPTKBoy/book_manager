# books = []
#
# def show_menu():
#     print('''
#     ==================================
#                 BOOK MANAGER
#     ==================================
#     1. Добавить книгу
#     2. Показать все книги
#     3. Найти книгу
#     4. Удалить книгу
#     5. Статистика
#     6. Изменить книгу
#     7. Показать только современные книги
#     8. Очистить библиотеку
#     0. Выход
#     ''')
#
# def add_book():
#     title = input("Введите название книги: ").strip()
#     author = input("Введите автора: ").strip()
#     year = input("Введите год выпуска: ").strip()
#
#     if title == "" or author == "":
#         print("Название и автор не могут быть пустыми")
#         return
#
#     if not year.isdigit():
#         print("Год должен быть числом")
#         return
#
#     year = int(year)
#     current_year = 2026
#
#     if year < 1500 or current_year < year:
#         print("Год должен быть от 1500 до", current_year)
#         return
#
#     exists = False
#     for book in books:
#         if book[0].lower() == title.lower():
#             exists = True
#
#     if exists:
#         print("Книга с таким названием уже есть в библиотеке")
#         return
#
#     books.append([title, author, year])
#     print("Книга успешно добавлена!")
#
# def show_books():
#     if len(books) == 0:
#         print("Библиотека пустая")
#         return
#
#     books.sort()
#
#     number = 1
#     for book in books:
#         print(str(number) + ". " + book[0] + " — " + book[1] + " (" + str(book[2]) + " год.)")
#         number = number + 1
#
#
# # Если вводить автора в поиске сделать так чтобы вводилось в конце сколько книги нашлось после успешнего поиска
#
# def find_book():
#     if len(books) == 0:
#         print("Библиотека пустая")
#         return
#
#     search = input("Введите названия книги или автора: ").strip().lower()
#
#     if search == "":
#         print("Введите текст для поиска")
#         return
#
#     count = 0
#     number = 1
#     for book in books:
#         if search in book[0].lower() or search in book[1].lower():
#             print(str(number) + ". " + book[0] + " - " + book[1] + " (" + str(book[2]) + ")")
#             count = count + 1
#         number = number + 1
#
#     if count == 0:
#         print("Найдено книг: 0")
#     else:
#         print("Найдено книг:", count)
#
# def delete_book():
#     if len(books) == 0:
#         print("Библиотека пустая")
#         return
#
#     show_books()
#     number = input("Введите номер книги: ").strip()
#
#     if not number.isdigit():
#         print("Неверный номер книги")
#         return
#
#     number = int(number)
#
#     if number < 1 or number > len(books):
#         print("Неверный номер книги")
#         return
#
#     book = books[number - 1]
#     books.pop(number - 1)
#     print("Книга " + book[0] + " удалена!")
#
# def show_statistics():
#     if len(books) == 0:
#         print("Библиотека пустая")
#         return
#
#     oldest = books[0][2]
#     newest = books[0][2]
#
#     for book in books:
#         if book[2] < oldest:
#             oldest = book[2]
#         if book[2] > newest:
#             newest = book[2]
#
#     print("Всего книг:", len(books))
#     print("Самая старая книга:", oldest)
#     print("Самая новая книга:", newest)
#
# def edit_book():
#     if len(books) == 0:
#         print("Библиотека пустая")
#         return
#
#     show_books()
#     number = input("Введите номер книги: ").strip()
#
#     if not number.isdigit():
#         print("Неверный номер книги")
#         return
#
#     number = int(number)
#
#     if number < 1 or number > len(books):
#         print("Неверный номер книги")
#         return
#
#     book = books[number - 1]
#
#     title = input("Новое название (Enter - оставить " + book[0] + "): ").strip()
#     author = input("Новый автор (Enter - оставить " + book[1] + "): ").strip()
#     year = input("Новый год (Enter - оставить " + str(book[2]) + "): ").strip()
#     if year != "":
#         if not year.isdigit():
#             print("Год должен быть числом, изменения не сохранены")
#             return
#         year = int(year)
#         current_year = 2026
#         if year < 1500 or current_year < year:
#             print("Год должен быть от 1500 до", current_year, "- изменения не сохранены")
#             return
#
#     if title == "" and author == "" and year == "":
#         print("Ничего не изменено")
#         return
#
#     if title != "":
#         book[0] = title
#
#     if author != "":
#         book[1] = author
#
#     if year != "":
#         book[2] = year
#
#     print("Книга изменена")
#
# def show_modern_books():
#     if len(books) == 0:
#         print("Библиотека пустая")
#         return
#
#     books.sort()
#
#     found = False
#     number = 1
#     year = input('Введите год: ').strip()
#     if not year.isdigit():
#         print("Год должен быть числом")
#         return
#
#     year = int(year)
#
#     if year < 1500 or year > 2026:
#         print("Неверный год книги")
#         return
#
#     for book in books:
#         if book[2] > year:
#             print(str(number) + ". " + book[0] + " — " + book[1] + " (" + str(book[2]) + " год.)")
#             found = True
#         number = number + 1
#
#     if not found:
#         print(f"Книг свыше {year} года нету")
#
#
#
#
# def clear_library():
#     if len(books) == 0:
#         print("Библиотека пустая")
#         return
#
#     print("Вы собираетесь удалить все книги:", len(books))
#     print("Это действие нельзя отменить!")
#     answer = input("Напишите УДАЛИТЬ чтобы подтвердить: ").strip()
#
#     if answer != "УДАЛИТЬ":
#         print("То что вы ввели не совпадает, библиотека не тронута")
#         return
#
#     books.clear()
#     print("Библиотека была очищена полностью")
#
#
# def main():
#     while True:
#         show_menu()
#         choice = input("Выберите действие: ")
#
#         if choice == "1":
#             add_book()
#         elif choice == "2":
#             show_books()
#         elif choice == "3":
#             find_book()
#         elif choice == "4":
#             delete_book()
#         elif choice == "5":
#             show_statistics()
#         elif choice == "6":
#             edit_book()
#         elif choice == "7":
#             show_modern_books()
#         elif choice == "8":
#             clear_library()
#         elif choice == "0":
#             print("Book manager остановлен спасибо что воспользовались нашим библиотекой.")
#             break
#         else:
#             print("Вы ввели не существующего меню")
#
#
# main()
#


import psycopg2

conn = psycopg2.connect(
    host="localhost",
    user="postgres",
    password="123456",
    port="5432",
    dbname="book_manager"
)

cursor = conn.cursor()

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
    7. Показать только современные книги
    8. Очистить библиотеку
    0. Выход
    ''')

def add_book():
    title = input("Введите название книги: ").strip()
    author = input("Введите автора: ").strip()
    year = input("Введите год выпуска: ").strip()

    if title == "" or author == "":
        print("Название и автора не могу быть пустыми")
        return

    if not year.isdigit():
        print("Год должен быть числом")
        return

    year = int(year)
    curren_year = 2026

    if year < 1500 or curren_year < year:
        print("Год должен быть от 1500 до", curren_year)
        return

    cursor.execute("SELECT id FROM books WHERE LOWER(title) = LOWER(%s)", (title,))
    found = cursor.fetchone()

    if found != None:
        print("Книга с таким названием уже есть в библиотеке")
        return

    cursor.execute("INSERT INTO books (title, author, year) VALUES (%s, %s, %s)", (title, author, year))
    conn.commit()
    print("Книга успешно добавлена!")

def show_books():
    cursor.execute("SELECT id, title, author, year FROM books ORDER BY title, author, year")
    rows = cursor.fetchall()

    if len(rows) == 0:
        print("Библиотека пустая")
        return rows

    number = 1
    for row in rows:
        print(str(number) + ". " + row[1] + " - " + row[2] + " (" + str(row[3]) + " год.)")
        number += 1

    return rows

def find_book():
    pass

def delete_book():
    pass

def show_statistics():
    pass

def edit_book():
    pass

def show_modern_books():
    pass

def clear_library():
    pass



def main():
    try:
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
            elif choice == "7":
                show_modern_books()
            elif choice == "8":
                clear_library()
            elif choice == "0":
                print("Book manager остановлен спасибо что воспользовались нашим библиотекой.")
                break
            else:
                print("Вы ввели не существующего меню")
    finally:
        cursor.close()
        conn.close()

main()
