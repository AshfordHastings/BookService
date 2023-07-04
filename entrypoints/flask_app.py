import json
from flask import Flask, jsonify, request, make_response
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from adapters.orm import start_mappers
from adapters.respository import SQLAlchemyRepository
from domain.model import Book, Author
from service_layer.services import update_author

# start_mappers()
# get_session = sessionmaker(bind=create_engine("sqlite:///:memory:"))
# session = get_session()

def create_app(session):
    app = Flask(__name__)

    @app.route("/books", methods=["POST"])
    def add_book():
        # session = get_session()
        book = Book(
            request.json["title"],
            request.json["year"]
        )
        SQLAlchemyRepository(session).add(book)
        return make_response({}, 201)

    @app.route("/books", methods=["GET"])
    def get_books():
        # session = get_session()

        SQLAlchemyRepository(session).lis
        return make_response({}, 201)
    
    @app.route("/books/<int:book_id>/update-author", methods=["POST"])
    def update_author_endpoint(book_id):
        book = SQLAlchemyRepository(session).get(Book, book_id)
        author = Author(
            request.json["first_name"],
            request.json["last_name"],
        )
        update_author(session, book, author)
        return make_response({}, 201)

    
    return app