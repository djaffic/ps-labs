books = {"Евгений Онегин": "Пушкин", "Капитанская дочка": "Пушкин", "Руслан и Людмила": "Пушкин", "Шурале": "Тукай", "Водяная": "Тукай", "Сказка о козе и баране": "Тукай"}


print("Название книг".ljust(30), "|", "Автор")
print("-"*40)
set_of_book = set()
for book, author in books.items():
    print(book.ljust(30), "|", author)

set_of_book.update(books)

uniq_authors = set()
print("Список всех произведений: ", set_of_book)

for author in books.values():
    uniq_authors.add(author)

print(uniq_authors)