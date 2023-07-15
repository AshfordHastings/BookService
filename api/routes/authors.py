from flask import Blueprint, request, g
from api.responses import response_with
import api.responses as resps
from service_layer.services import (
    create_author
)

author_bp = Blueprint('author', __name__)


@author_bp.route("/authors", methods=["POST"])
def create_new_author():
    session = g.db_session
    #TODO: Create author returns an existing author if it isn't created... need to handle it, or something.

    result = create_author(
            session,
            first_name = request.json["first_name"],
            last_name = request.json["last_name"]
        )

    return response_with(resps.SUCCESS_201, value=result)
