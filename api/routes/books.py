from flask import Blueprint, request, g, make_response
from BookService.domain.schemas.book import AuthorSchema, BookSchema
from domain.model.book import BookObject, Book, MData, Author
from sqlalchemy import select 
from marshmallow import EXCLUDE
from api.responses import response_with
import api.responses as resps
from service_layer.services import (
    create_book_and_optionally_create_author
)

book_bp = Blueprint('book', __name__)
book_schema = BookSchema(unknown=EXCLUDE)
author_schema = AuthorSchema()

@book_bp.route("/books", methods=["GET"])
def get_book_list():
    session = g.db_session

    stmt = select(Book).order_by(Book.id)
    books = session.scalars(stmt).all()
    return response_with(resps.SUCCESS_200, value=books)

@book_bp.route("/books", methods=["POST"])
def create_book_and_optionally_create_author_endpoint():

    #TODO: Have option to upload a book without an author, update code accordingly 
    #TODO: Reimplement data session commits across the app.
    #TODO: Implement error handling to return error response in invalid request body    

    session = g.db_session

    book = book_schema.load(request.json)
    author = author_schema.load(request.json["author"]) if request.json.get("author") else None

    try:
        result = create_book_and_optionally_create_author(session, book, author)
    except Exception:
        return make_response(resps.ERROR_400, error="Author is not included in the request.")

    return response_with(resps.SUCCESS_201, value=result)

@book_bp.route("/books/<int:book_id>", methods=["GET"])
def get_book_resouces(book_id):
    session = g.db_session

    stmt = select(Book).where(Book.id == book_id)
    book = session.scalars(stmt).first()

    if book == None: return make_response({}, 404)
    return response_with(resps.SUCCESS_200, value=book)