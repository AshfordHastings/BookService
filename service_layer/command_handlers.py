from typing import List
from sqlalchemy import select
from sqlalchemy.orm import Session

from domain import commands
from domain.model.book import Book, Author
from domain import events

#TODO: Implement something similar to an interface, but for functions

def create_author(session:'Session', queue:List['Message'], command: 'commands.CreateAuthor'):
    #TODO: Make it not be "first" make it check the length
    #TODO: Run event for author being created! Right? It's not committed? 
        # Raise Author already exists error. Handle the error on the outside (SRP). Do the same in both functions.
        # If I am implementing logic like this, first_name and last_name should be a unique composite in the schema.

    get_author = session.scalars(
        select(Author).where(
            Author.first_name == command.author.first_name and
            Author.last_name == command.author.last_name
        )).first()
    
    if get_author:
        print("Author exists in the database already.")
        return get_author

    session.add(command.author)
    session.flush() #Need to flush so author gets assigned an id, consider doing this outside
    queue.append(events.AuthorCreated(command.author))
    return command.author        

def create_book(session:'Session', queue:List['Message'], command: 'commands.CreateBook'):
    # TODO: Implement Error Handling
    session.add(command.book)
    queue.append(events.BookCreated(command.book.id, command.book.author_id))
    return command.book

