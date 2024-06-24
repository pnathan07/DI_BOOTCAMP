class Book:
    def __init__(self, title, author, publication_date, price):
        self.title = title
        self.author = author
        self.publication = publication_date
        self.price = price

    def present(self):
        print(f'Title: {self.title}')

class Fiction(Book):
    def __init__(self, title, author, publication_date, price, is_awasome):
        super().__init__(title, author, publication_date, price)
        self.genre = 'Fiction'
        self.is_awasome = is_awasome
        if self.is_awasome:
            self.bored = False
        else:
            self.bored = True


book1 = Fiction('1984', 'George Orwell', 1948, 100, False)
print(book1.bored)