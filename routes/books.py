from flask import Blueprint, request, g, make_response
from domain.model import BookObject, Book, MData, Author
from sqlalchemy import select 

book_bp = Blueprint('book', __name__)

@book_bp.route("/books", methods=["POST"])
def add_book():
    session = g.db_session

    a = session.scalars(select(Author).where(
        Author.first_name==request.json["first_name"] and
        Author.last_name==request.json["last_name"]
    )).first()
    if a is None: print("a is none") 
    print(a)
    if a is None:
        a = Author(
            request.json["first_name"],
            request.json["last_name"]
        )

    book = BookObject(
        Book(
            request.json["title"],
            request.json["year"],
            a
        ),
        MData(
            request.json["extension"]
        )
    )
    
    session.add(book)
    session.commit()

    return make_response({}, 201)

# @book_bp.route("/books", methods=["GET"])
# def get_books():
#     # session = get_session()

#     SQLAlchemyRepository(session).lis
#     return make_response({}, 201)

# @book_bp.route("/books/<int:book_id>/update-author", methods=["POST"])
# def update_author_endpoint(book_id):
#     book = SQLAlchemyRepository(session).get(Book, book_id)
#     author = Author(
#         request.json["first_name"],
#         request.json["last_name"],
#     )
#     update_author(session, book, author)
#     return make_response({}, 201)
