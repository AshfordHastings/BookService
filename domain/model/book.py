from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship, composite
from dataclasses import dataclass

from . import Base
from host import Host

# class MData(Base):
#     __tablename__ = "m_data"
#     id: Mapped[int] = mapped_column(primary_key=True)
#     ext: Mapped[str]

#     def __composite_values__(self):
#         return (self.ext)

#     def __eq__(self, other):
#         return isinstance(other, MData) and other.ext == self.ext
    
#     def __ne__(self, other):
#         return not self._eq__(other)

#     def __init__(self, ext):
#         self.ext = ext


@dataclass
class MData:
    ext: str

class Author(Base):
    __tablename__ = "author"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    first_name: Mapped[str] = mapped_column(nullable=False)
    last_name: Mapped[str]

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    def __json__(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name
        }
    


class Book(Base):
    __tablename__ = "book"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str]
    year: Mapped[int]
    author_id: Mapped[int] = mapped_column(ForeignKey("author.id"))

    author: Mapped['Author'] =  relationship()

    def __init__(self, title, year, author):
        self.title = title
        self.year = year
        self.author = author

    def __eq__(self, other):
        return isinstance(other, Book) and self.id == other.id
    
    def __json__(self):
        return {
            'id': self.id,
            'title': self.title,
            'year': self.year,
            'author': self.author.__json__()
        }


class BookObject(Base):
    __tablename__ = "book_object"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    book_id: Mapped[int] = mapped_column(ForeignKey("book.id"))
    host_id: Mapped[Host] = mapped_column(ForeignKey("host.id"))

    m_data: Mapped['MData'] = composite(mapped_column("ext"))
    book: Mapped['Book'] = relationship()
    host: Mapped['Host'] = relationship(back_populates='Host')

    def __init__(self, book, m_data):
        self.book = book
        self.m_data = m_data

    def get_book_content(self):
        return self.host(self)