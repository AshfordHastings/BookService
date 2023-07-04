from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Dict, List, Tuple
from pathlib import Path
from uuid import UUID, uuid4

AuthorID = UUID
BookID = UUID

@dataclass
class Author:
    first_name: str
    last_name: str
    id: AuthorID = uuid4()
@dataclass 
class BookMetadata:
    file_extension: str
@dataclass
class BookInfo:
    title: str
    year: int
    author: Author

class Book:
    def __init__(self, info:BookInfo, metadata: BookMetadata, id:BookID=uuid4()):
        self.id = id
        self.info = info
        self.book = metadata

class Shelf:
    def __init__(self, host:'Host', books:Dict[str, Book]={}):
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
    def store_book_content(self, book:Book, content:bytes):
        pass
class DirHost(Host):
    def __init__(self, base_dir):
        self.base_dir = base_dir
    def get_book_content(self, book:Book) -> bytes:
        loc = self.base_dir / format_book_filename(book)
        return loc.read_bytes()
    def store_book_content(self, book:Book, content:bytes) -> None:
        loc = self.base_dir / format_book_filename(book)
        loc.parents[0].mkdir(parents=True, exist_ok=True)
        loc.write_bytes(content)

class TempHost(Host):
    def __init__(self, in_mem_content={}):
        self.in_mem_content = in_mem_content
    def get_book_content(self, book:Book) -> bytes:
        return self.in_mem_content.get(book.id)
    def store_book_content(self, book:Book, content:bytes) -> None:
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


