    # @app.route("/books", methods=["POST"])
    # def add_book():
    #     # session = get_session()
    #     book = Book(
    #         request.json["title"],
    #         request.json["year"]
    #     )
    #     SQLAlchemyRepository(session).add(book)
    #     return make_response({}, 201)