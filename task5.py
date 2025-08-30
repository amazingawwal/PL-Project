class Books():
    def __init__(self, title):
        self.total_books = 12
        self.library_id = "GK101L"
        self.title = title

    def add_books(self, number):
        self.total_books+=number
        print(f"You have added {number} books to {self.title}. You have a total of {self.total_books} books now")

    def remove_books(self, number):
        self.total_books-=number
        print(f"You have removed {number} books. You now have {self.total_books} books left")

    def count_books(self):
        print(f"You have {self.total_books} books in your library")



books = Books("Harry Potter")
books.add_books(3)
books.count_books()
print(books.title)


class Library(Books):
    def add_books(self, number):
        self.total_books+=number
        print(f"You have added {number} books to {self.title}. You have a total of {self.total_books} now")

    def count_books(self):
        print(f"You have {self.total_books} books in your library")

library = Library("LOTS 3")
print(library.title)
library.add_books(5)
library.count_books()