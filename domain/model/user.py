from typing import Set
from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from . import Base
from book import BookObject
import domain.events as events

user_book_views_table = Table(
    "user_views_book_table",
    Base.metadata,
    Column("user", ForeignKey("user.id"), primary_key=True),
    Column('book_object_view', ForeignKey("book_object.id"), primary_key=True),
)

class User(Base):
    __tablename__ = 'user'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    username: Mapped[str]
    display_name: Mapped[str]

    book_views: Mapped[Set['BookObject']] = relationship(secondary=user_book_views_table)

    def __init__(self, username, display_name):
        self.username = username
        self.display_name = display_name
        self.book_views = set()
        self.events = []

    @property
    def book_views_this_month(self):
        return len(self.book_views)
    
    def get_book(self, book:BookObject):
        if self.book_views_this_month >= 5:
            self.events.append(events.BookLimitReached(self.id))
            return None
        content = book.get_book_content(book)
        self.book_views.add(book)
        return content 