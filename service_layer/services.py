from adapters.respository import AbstractRepository
from domain.model import Book, Author, User, BookObject

def update_author(repo:AbstractRepository, book:Book, author:Author):
    current_author = book._author
    current_author._books.remove(book)
    author.add_book(book)
    repo.add_all([book, author, current_author])

def user_views_book(session, user:User, book:BookObject):
    if user.book_views_this_month >= 5:
        raise Exception
    book_content = book.get_book_content()
    user.book_views.add(book)
    if user.book_views_this_month >= 5:
        print('Alert! Max number of books reached!')
    session.commit()
    # Check number of Book user has viewed this month
    # Check that book user wants to view is extant
    # Get book user wants to view
    # Increment number of books user has viewed this month 
    # Send alert that user is out of books if the limit has been hit 


