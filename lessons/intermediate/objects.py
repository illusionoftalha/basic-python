"""Keep state and the operations that protect it together."""

from dataclasses import dataclass


@dataclass
class Book:
    title: str
    borrowed: bool = False

    def borrow(self):
        if self.borrowed:
            raise ValueError("book is already borrowed")
        self.borrowed = True

    def return_book(self):
        self.borrowed = False


if __name__ == "__main__":
    book = Book("Learning Python")
    book.borrow()
    print(f"{book.title}: borrowed={book.borrowed}")
    book.return_book()
    print(f"{book.title}: borrowed={book.borrowed}")
