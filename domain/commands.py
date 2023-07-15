from dataclasses import dataclass
from domain.model.book import Author, Book


class Command:
    pass

@dataclass
class CreateBook(Command):
    book: Book

@dataclass
class CreateAuthor(Command):
    author: Author
