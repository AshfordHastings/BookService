from adapters.respository import AbstractRepository
from domain.model import Book, Author

def update_author(repo:AbstractRepository, book:Book, author:Author):
    current_author = book._author
    current_author._books.remove(book)
    author.add_book(book)
    repo.add_all([book, author, current_author])
