from typing import List
from dataclasses import dataclass

# @dataclass(unsafe_hash=True)
# class Book:
#     title: str
#     year: int

class Book:
    def __init__(self, title, year, author=None):
        self.title = title
        self.year = year
        self._author = author
    
# class HTMLBook:
#     def __init__(self, title, year):
#         self.title = title
#         self.year = year
#     def get_content(self):
#         return f"<h1>{self.title}</h1>"
# class EPUBBook:
#     def __init__(self, title, year):
#         return f"EPUB format of {title}"
        
class Author:
    def __init__(self, first_name:str, last_name:str):
        self.first_name = first_name
        self.last_name = last_name
        self._books = set()
    def add_book(self, book:Book) -> None:
        self._books.add(book)
        book._author = self
    def add_books(self, books:List[Book]) -> None:
        for book in books: book._author = self
        self._books.update(books)
    @property
    def num_books_written(self) -> int:
        return len(self._books)
    @property
    def books_written(self) -> List[Book]:
        return self._books

