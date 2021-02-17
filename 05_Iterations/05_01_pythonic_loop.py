books = ['1984', 'Ash', 'Beloved']
i = 0
while i < len(books):
    print(books[i])
    i += 1

for book in books:
    print(book)

for i, book in enumerate(books):
    print(f'{i}: {book}')

students = {
    'Alice': 20,
    'Bob': 19
}

for name, age in students.items():
    print(f'{name} is {age} years old.')

for i in range(2, 17, 3):
    print(i)
