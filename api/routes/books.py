from flask import Blueprint, request, g, make_response
from domain.model.book import BookObject, Book, MData, Author
from sqlalchemy import select 
from api.responses import response_with, SUCCESS_200
from domain import commands, events
from service_layer import messagebus

book_bp = Blueprint('book', __name__)


@book_bp.route("/books", methods=["GET"])
def get_books():
    session = g.db_session

    stmt = select(Book).order_by(Book.id)
    books = session.scalars(stmt).all()
    return response_with(SUCCESS_200, value=books)

@book_bp.route("/books/<int:book_id>", methods=["GET"])
def get_book(book_id):
    session = g.db_session

    stmt = select(Book).where(Book.id == book_id)
    book = session.scalars(stmt).first()

    if book == None: return make_response({}, 404)
    return response_with(SUCCESS_200, value=book)


@book_bp.route("/books", methods=["POST"])
def add_book():
    session = g.db_session
    # Maybe implement custom create or get method util?
    command = commands.CreateBook(
        request.json["title"], 
        request.json["year"], 
        Author(
            request.json["first_name"],
            request.json["last_name"]
        )
    )
    messagebus.handle(command, session)
    return make_response({}, 201)



    a = session.scalars(select(Author).where(
        Author.first_name==request.json["first_name"] and
        Author.last_name==request.json["last_name"]
    )).first()
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
