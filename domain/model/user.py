from typing import Set
from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from . import Base
from book import BookObject

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

    @property
    def book_views_this_month(self):
        return len(self.book_views)
