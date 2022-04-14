# 1.Старата библиотека
# Ани отива до родния си град след много дълъг период извън страната. Прибирайки се вкъщи, тя вижда старата библиотека на баба си и си спомня за любимата си книга. Помогнете на Ани, като напишете програма, в която тя въвежда търсената от нея книга (текст). Докато Ани не намери любимата си книга или не провери всички книги в библиотеката, програмата трябва да чете всеки път на нов ред името на всяка следваща книга (текст), която тя проверява. Книгите в библиотеката са свършили щом получите текст "No More Books".
# Ако не открие търсената книгата да се отпечата на два реда:
# o"The book you search is not here!"
# o"You checked {брой} books."
# Ако открие книгата си се отпечатва един ред:
# "You checked {брой} books and found it."
#
# Вход
# Troy
# Stronger
# Life Style
# Troy
#
# Изход
# You checked 2 books and found it.

book_name = input()

current_book = input()
books_count = 0

while current_book != "No More Books":
    if current_book == book_name:
        print(f"You checked {books_count} books and found it.")
        break
    books_count += 1
    current_book = input()

if current_book != book_name:
    print("The book you search is not here!")
    print(f"You checked {books_count} books.")
