from abc import ABC, abstractmethod
from typing import Dict, Tuple
from pathlib import Path
from sqlalchemy.orm import Mapped, mapped_column

from . import Base
#from domain.model.book import BookObject, Book
#import domain.model.book as book
#from . import book

# class Shelf:
#     def __init__(self, host:'Host', books:Dict[str, BookObject]={}):
#         self.host = host
#         self._books= books

#     def get_book_and_content(self, id:str) -> Tuple[Book, bytes]:
#         book = self._books[id]
#         content = self.host.get_book_content(book)
#         return (book, content)
    
#     def store_book_and_content(self, book:Book, content:bytes) -> None:
#         self.host.store_book_content(book, content)
#         self._books.update({book.id: book})

class Host(Base):
    __tablename__ = "host"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    type: Mapped[str]

    __mapper_args__ = {
        "polymorphic_on": "type",
        "polymorphic_abstract": True
    }

    def get_book_content() -> bytes:
        pass
    def store_book_content(self, book:'BookObject', content:bytes):
        pass

class AzureBlobStorageHost(Host):
    url: Mapped[str] = mapped_column(nullable=True)
    container: Mapped[str] = mapped_column(nullable=True)
    
    __mapper_args__ = {
        "polymorphic_identity": "azure_blob_container"
    }

class DirHost(Host):
    base_dir: Mapped[str] = mapped_column(nullable=True)

    __mapper_args__ = {
        "polymorphic_identity": "local_directory"
    }

    def __init__(self, base_dir):
        self.base_dir = base_dir
    def get_book_content(self, book:'BookObject') -> bytes:
        loc = self.base_dir / format_book_filename(book)
        return loc.read_bytes()
    def store_book_content(self, book:'BookObject', content:bytes) -> None:
        loc = self.base_dir / format_book_filename(book)
        loc.parents[0].mkdir(parents=True, exist_ok=True)
        loc.write_bytes(content)

class TempHost(Host):
    __mapper_args__ = {
        "polymorphic_identity": "in_memory"
    }

    def __init__(self, in_mem_content={}):
        self.in_mem_content = in_mem_content
    def get_book_content(self, book:'BookObject') -> bytes:
        return self.in_mem_content.get(book.id)
    def store_book_content(self, book:'BookObject', content:bytes) -> None:
        self.in_mem_content.update({ book.id: content })

def format_book_filename(book:'Book') -> Path:
    p =  Path() \
        / f"{book.book_info.author.last_name}_{book.book_info.author.first_name}" \
        / f"{book.book_info.title.replace(' ' , '_')}" \
        / f"{book.id}.{book.book_format.ext}"
    print(f"{book.id}.{book.book_format.ext}")
    return p
