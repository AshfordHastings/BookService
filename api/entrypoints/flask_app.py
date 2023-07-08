from flask import Flask, g

from api.routes import book_bp

def create_app(session):
    app = Flask(__name__)

    @app.before_request
    def before_request():
        g.db_session = session

    @app.after_request
    def teardown_request(response):
        db_session = getattr(g, 'db_session', None)
        if db_session is not None:
            db_session.close()
        return response

    app.register_blueprint(book_bp)
    
    return app