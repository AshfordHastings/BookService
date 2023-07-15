import pytest
import config


def test_get_book_returns_book_and_200(client, persisted_book):
    book_id = persisted_book.id
    url = config.get_api_url()
    resp = client.get(f"{url}/books/{book_id}")
    assert resp.status_code == 200
    val = resp.json.get('value')
    assert val['id'] == persisted_book.id
    assert val['title'] == persisted_book.title
    assert val['author_id'] == persisted_book.author_id

@pytest.mark.usefixtures('persisted_book_list')
def test_get_book_list(client):
    # TODO: Validate json output for its values  
    url = config.get_api_url()
    resp = client.get(f"{url}/books")
    assert resp.status_code == 200
    assert len(resp.json['value']) == 3


def test_create_book_returns_201(client):
    data = {
        "title": "Grapes of Wrath",
        "year": 1937,
        "author": {
            "first_name": "John",
            "last_name": "Steinbeck"
        }
    }
    url = config.get_api_url()
    resp = client.post(f"{url}/books", json=data)
    assert resp.status_code == 201
    assert resp.json["value"]
    print(resp.json["value"])

@pytest.mark.usefixtures('persisted_author')
def test_create_book_with_persisted_author_returns_201(client):
    data = {
        "title": "Grapes of Wrath",
        "year": 1937,
        "author": {
            "first_name": "John",
            "last_name": "Steinbeck"
        }
    }
    url = config.get_api_url()
    resp = client.post(f"{url}/books", json=data)
    assert resp.status_code == 201
    assert resp.json["value"]
    print(resp.json["value"])

def test_create_book_with_author_id_returns_201(client, persisted_author):
    data = {
        "title": "Grapes of Wrath",
        "year": 1937,
        "author_id": persisted_author.id
    }
    url = config.get_api_url()
    resp = client.post(f"{url}/books", json=data)
    assert resp.status_code == 201
    assert resp.json["value"]
    print("Hello")
    print(resp.json["value"])
def test_create_author(client):
    data = {
        "first_name": "John",
        "last_name": "Steinbeck"
    }
    url = config.get_api_url()
    resp = client.post(f"{url}/authors", json=data)
    assert resp.status_code == 201
    assert resp.json["value"]
    print(resp.json["value"])