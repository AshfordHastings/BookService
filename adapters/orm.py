from sqlalchemy import Integer, String, ForeignKey, Table, Column
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, registry, relationship
from sqlalchemy import Uuid
from typing import List
from domain.model import Book, Author

# ID = UUID(as_uuid=True)

class Base(DeclarativeBase):
    pass

class AuthorModel(Base):
    __tablename__ = "author"
    id: Mapped[Uuid(as_uuid=True)] = mapped_column(primary_key=True)
    first_name: Mapped[str]
    last_name: Mapped[str]

    books: Mapped[List['BookModel']] = relationship(back_populates='author')

class BookModel(Base):
    __tablename__ = "book"

    id: Mapped[Uuid(as_uuid=True)] = mapped_column(primary_key=True)
    title: Mapped[str]
    year: Mapped[int]
    file_extension: Mapped[str]
    author_id: Mapped[int] = mapped_column(ForeignKey("author.id"))

    author: Mapped['AuthorModel'] =  relationship(back_populates='books')
