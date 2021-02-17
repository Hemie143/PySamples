books = ['1984', 'Ash', 'Beloved']
i = 0
while i < len(books):
    print(books[i])
    i += 1

for book in books:
    print(book)

for i, book in enumerate(books):
    print(f'{i}: {book}')
