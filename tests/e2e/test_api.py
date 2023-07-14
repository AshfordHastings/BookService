import pytest, requests, json

from domain.model.book import Book, Author
from api.schemas.book import BookSchema
import config

def create_persisted_author(session, first_name, last_name):
    author = Author(
        first_name=first_name,
        last_name=last_name
    )
    session.add(author)
    session.commit()
    return author

def create_persisted_book(session, title, year, persisted_author):
    book = Book(
        title,
        year,
        author=persisted_author
    )
    session.add(book)
    session.commit()
    return book

@pytest.fixture()
def persisted_book_list(session):
    b_list = [('Of Mice and Men', 1937), ('Grapes of Wrath', 1945), ('The Pearl', 1951)]
    a = create_persisted_author(session, 'John', 'Steinbeck')
    return [create_persisted_book(session, b[0], b[1], a) for b in b_list]

@pytest.fixture()
def persisted_author(session):
    return create_persisted_author(session, 'John', 'Steinbeck')

@pytest.fixture()
def persisted_book(session, persisted_author):
    return create_persisted_book(session, "Grapes of Wrath", 1937, persisted_author)

@pytest.mark.skip(reason="Unfinished test.")
def test_post_book_returns_2011(client):
    data = {"title": "Grapes of Wrath", "year": 1937}
    url = config.get_api_url()
    resp = client.post(f"{url}/books", json=data)
    assert resp.status_code == 201

@pytest.mark.skip(reason="Unfinished test.")
def test_get_book_returns_book_and_200(client, persisted_book):
    book_id = persisted_book.id
    url = config.get_api_url()
    resp = client.get(f"{url}/books/{book_id}")
    assert resp.status_code == 200
    val = resp.json.get('value')
    assert val['id'] == persisted_book.id
    assert val['title'] == persisted_book.title
    assert val['author']['first_name'] == persisted_book.author.first_name

@pytest.mark.skip(reason="Unfinished test.")
def test_get_book_list(client, persisted_book_list):
    url = config.get_api_url()
    resp = client.get(f"{url}/books")
    assert resp.status_code == 200
    book_schema = BookSchema(many=True)
    #assert resp.json["value"] == book_schema.dump(persisted_book_list)
    print(resp.json)
    # assert resp.json.get("value")
    # assert len(resp.json.get("value")) == 3


def test_create_book_returns_201(client):
    data = {
        "title": "Grapes of Wrath",
        "year": 1937,
        "first_name": "John",
        "last_name": "Steinbeck",
        "extension": "txt"
    }
    url = config.get_api_url()
    resp = client.post(f"{url}/books", json=data)
    assert resp.status_code == 201