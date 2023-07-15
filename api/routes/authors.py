from flask import Blueprint, request, g
from BookService.domain.schemas.book import AuthorSchema
from api.responses import response_with
import api.responses as resps
from service_layer.services import (
    create_author
)

author_bp = Blueprint('author', __name__)
author_schema = AuthorSchema()

@author_bp.route("/authors", methods=["POST"])
def create_new_author():
    session = g.db_session
    #TODO: Create author returns an existing author if it isn't created... need to handle it, or something.

    author = author_schema.load(request.json)
    
    try:
        result = create_author(session, author)
    except Exception:
        return response_with(resps.ERROR_400, error="Author is not included in the request.")

    return response_with(resps.SUCCESS_201, value=result)
