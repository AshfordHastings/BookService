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
def create_author(session:Session, author: 'Author'):
    results = messagebus.handle(
        session,
        commands.CreateAuthor(
            author
        ),
    )
    created_author = results.pop()
    return created_author

def create_book(session:Session, book: 'Book'):
    results = messagebus.handle(
        session,
        commands.CreateBook(
            book
        )
    )
    created_book = results.pop()
    return created_book

def create_book_and_optionally_create_author(session:Session, book:'Book', author:'Author'=None):
    #TODO: Unit of work should stop and end inside of this service function (?)
    if not book.author_id and not author:
        raise Exception("Either 'author_id' or 'author' is required.")
    if book.author_id and author:
        raise Exception("Cannot create an author and create a book with reference to an existing author.")
    
    if author:
        created_author = create_author(session, author)
        book.author_id = created_author.id

    created_book = create_book(session, book)
    return created_book