import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, clear_mappers
from sqlalchemy.exc import OperationalError
from pathlib import Path
import time
#from entrypoints.flask_app import create_app
import config


@pytest.fixture()
def in_memory_db():
    engine = create_engine(config.get_sqlite_url())
    #mapper_registry.metadata.create_all(engine)
    return engine

@pytest.fixture()
def session(in_memory_db):
    #start_mappers()
    yield sessionmaker(bind=in_memory_db)()
    #clear_mappers()

# @pytest.fixture()
# def client(session):
#     app = create_app(session)
#     with app.test_client() as client:
#         with app.app_context():
#             yield client


