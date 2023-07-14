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
    assert val['author']['first_name'] == persisted_book.author.first_name

@pytest.mark.usefixtures('persisted_book_list')
def test_get_book_list(client):
    # TODO: Validate json output for its values  
    url = config.get_api_url()
    resp = client.get(f"{url}/books")
    assert resp.status_code == 200
    assert len(resp.json['value']) == 3
    
    # assert resp.json.get("value")
    #book_schema = BookSchema(many=True)
    #assert resp.json["value"] == book_schema.dump(persisted_book_list)
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