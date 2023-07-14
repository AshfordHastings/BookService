from dataclasses import dataclass
from domain.model.book import Author


class Command:
    pass

@dataclass
class CreateBook(Command):
    title: str
    year: int
    author: Author