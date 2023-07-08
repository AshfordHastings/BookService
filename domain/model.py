from abc import ABC, abstractmethod
from typing import Dict, List, Tuple
from pathlib import Path
from sqlalchemy import ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship, composite
from dataclasses import dataclass

class Base(DeclarativeBase):
    pass

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

    m_data: Mapped['MData'] = composite(mapped_column("ext"))
    book: Mapped['Book'] = relationship()

    # __mapper_args__ = {
    #     "polymorphic_on": "type",
    #     "polymorphic_identity": "book"
    # }

    def __init__(self, book, m_data):
        self.book = book
        self.m_data = m_data






# @dataclass
# class Author:
#     first_name: str
#     last_name: str
#     id: AuthorID = uuid4()
# @dataclass 
# class BookMetadata:
#     file_extension: str
# @dataclass
# class BookInfo:
#     title: str
#     year: int
#     author: Author

# class Book:
#     def __init__(self, info:BookInfo, metadata: BookMetadata, id:BookID=uuid4()):
#         self.id = id
#         self.info = info
#         self.book = metadata

class Shelf:
    def __init__(self, host:'Host', books:Dict[str, BookObject]={}):
        self.host = host
        self._books= books

    def get_book_and_content(self, id:str) -> Tuple[Book, bytes]:
        book = self._books[id]
        content = self.host.get_book_content(book)
        return (book, content)
    
    def store_book_and_content(self, book:Book, content:bytes) -> None:
        self.host.store_book_content(book, content)
        self._books.update({book.id: book})

class Host(ABC):
    @abstractmethod
    def get_book_content():
        pass
    @abstractmethod
    def store_book_content(self, book:BookObject, content:bytes):
        pass
class DirHost(Host):
    def __init__(self, base_dir):
        self.base_dir = base_dir
    def get_book_content(self, book:BookObject) -> bytes:
        loc = self.base_dir / format_book_filename(book)
        return loc.read_bytes()
    def store_book_content(self, book:BookObject, content:bytes) -> None:
        loc = self.base_dir / format_book_filename(book)
        loc.parents[0].mkdir(parents=True, exist_ok=True)
        loc.write_bytes(content)

class TempHost(Host):
    def __init__(self, in_mem_content={}):
        self.in_mem_content = in_mem_content
    def get_book_content(self, book:BookObject) -> bytes:
        return self.in_mem_content.get(book.id)
    def store_book_content(self, book:BookObject, content:bytes) -> None:
        self.in_mem_content.update({ book.id: content })

def format_book_filename(book:Book) -> Path:
    p =  Path() \
        / f"{book.book_info.author.last_name}_{book.book_info.author.first_name}" \
        / f"{book.book_info.title.replace(' ' , '_')}" \
        / f"{book.id}.{book.book_format.ext}"
    print(f"{book.id}.{book.book_format.ext}")
    return p

if __name__ == '__main__':
    pass


