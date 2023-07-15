import service_layer.messagebus as messagebus
from domain import commands
from sqlalchemy.orm import Session

# def update_author(repo:AbstractRepository, book:Book, author:Author):
#     current_author = book._author
#     current_author._books.remove(book)
#     author.add_book(book)
#     repo.add_all([book, author, current_author])

# def user_views_book(session, user:User, book:BookObject):
#     if user.book_views_this_month >= 5:
#         raise Exception
#     book_content = book.get_book_content()
#     user.book_views.add(book)
#     if user.book_views_this_month >= 5:
#         print('Alert! Max number of books reached!')
#     session.commit()
    # Check number of Book user has viewed this month
    # Check that book user wants to view is extant
    # Get book user wants to view
    # Increment number of books user has viewed this month 
    # Send alert that user is out of books if the limit has been hit 

#TODO: Update to allow Authors and Books to be passed in as object maybe? 
def create_author(session:Session, first_name, last_name):
    author = messagebus.handle(
        commands.CreateAuthor(
            first_name,
            last_name
        ),
        session
    )
    return author

def create_book_with_author_id(session:Session, title, year, author_id):
    book = messagebus.handle(
        commands.CreateBook(
            title,
            year,
            author_id
        ),
        session
    )    
    return book

def create_book_and_author(session:Session, title, year, first_name, last_name):
    author = create_author(session, first_name, last_name)
    book = create_book_with_author_id(session, title, year, author.id)
    return book
