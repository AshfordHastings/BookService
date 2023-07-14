from sqlalchemy import select
from sqlalchemy.orm import Session

from domain import commands
from domain.model.book import BookObject, Book, MData, Author

def create_book(command: commands.CreateBook, session:Session):
    a = session.scalars(select(Author).where(
        Author.first_name == command.author.first_name and
        Author.last_name == command.author.last_name
    )).first()
    if a is None:
        a = Author(
            command.author.first_name,
            command.author.last_name
        )
    book = Book(
        command.title,
        command.year,
        a
    )
    session.add(book)
    print("Book has been created!")