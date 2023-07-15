from flask import Blueprint, request, g, make_response
from domain.model.book import BookObject, Book, MData, Author
from sqlalchemy import select 
from api.responses import response_with
import api.responses as resps
from service_layer.services import (
    create_book_with_author_id,
    create_book_and_author
)

book_bp = Blueprint('book', __name__)


@book_bp.route("/books", methods=["GET"])
def get_books():
    session = g.db_session

    stmt = select(Book).order_by(Book.id)
    books = session.scalars(stmt).all()
    return response_with(resps.SUCCESS_200, value=books)

@book_bp.route("/books/<int:book_id>", methods=["GET"])
def get_book(book_id):
    session = g.db_session

    stmt = select(Book).where(Book.id == book_id)
    book = session.scalars(stmt).first()

    if book == None: return make_response({}, 404)
    return response_with(resps.SUCCESS_200, value=book)


@book_bp.route("/books", methods=["POST"])
def create_book():
    session = g.db_session
    #TODO: Separate validation into another component (Marshmallwow?)
    #TODO: Have option to upload a book without an author, update code accordingly 
    if request.json.get("author_id"):
         result = create_book_with_author_id(
            session,
            title = request.json["title"],
            year = request.json["year"],
            author_id = request.json["author_id"]
        )
    elif request.json.get("author"):
        result = create_book_and_author(
            session,
            title = request.json["title"],
            year = request.json["year"],
            first_name = request.json["author"]["first_name"],
            last_name = request.json["author"]["first_name"]
        )
    else:
        return make_response(resps.ERROR_400, error="Author is not included in the request.")

    return response_with(resps.SUCCESS_201, value=result)

# @book_bp.route("/authors", methods=["POST"])
# def create_a():
#     session = g.db_session
#     #TODO: Separate validation into another component (Marshmallwow?)
#     #TODO: Have option to upload a book without an author, update code accordingly 
#     if request.json.get("author_id"):
#          result = create_book_with_author_id(
#             session,
#             title = request.json["title"],
#             year = request.json["year"],
#             author_id = request.json["author_id"]
#         )
#     elif request.json.get("author"):
#         result = create_book_and_author(
#             session,
#             title = request.json["title"],
#             year = request.json["year"],
#             first_name = request.json["author"]["first_name"],
#             last_name = request.json["author"]["first_name"]
#         )
#     else:
#         return make_response(resps.ERROR_400, error="Author is not included in the request.")

#     return response_with(resps.SUCCESS_201, value=result)

# @book_bp.route("/books/<int:book_id>/update-author", methods=["POST"])
# def update_author_endpoint(book_id):
#     book = SQLAlchemyRepository(session).get(Book, book_id)
#     author = Author(
#         request.json["first_name"],
#         request.json["last_name"],
#     )
#     update_author(session, book, author)
#     return make_response({}, 201)
