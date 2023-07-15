from sqlalchemy import select
from sqlalchemy.orm import Session

from domain import commands
from domain.model.book import Book, Author

def create_author(command: 'commands.CreateAuthor', session:'Session'):
    #TODO: Make it not be "first" make it check the length
    get_author = session.scalars(select(Author).where(
        #TODO: Update these if we put author into the command
        Author.first_name == command.first_name and
        Author.last_name == command.last_name
    )).first()
    if not get_author:
        new_author = Author(
            first_name=command.first_name,
            last_name=command.last_name
        )
        session.add(new_author)
        session.flush() #Need to flush so author gets assigned an id, consider doing this outside
        #TODO: Run event for author being created! Right? It's not committed? 
        return new_author
    else:
        print("Author exists in the database already.")
        return get_author
        

def create_book(command: 'commands.CreateBook', session:'Session'):
    # TODO: Implement Error Handling
    book = Book(
        command.title,
        command.year,
        command.author_id
    )
    session.add(book)
    return book

