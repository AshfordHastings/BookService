import pytest, requests
from flask import g

import config

@pytest.mark.skip(reason="Unfinished test.")
def test_post_book_returns_2011(client):
    data = {"title": "Grapes of Wrath", "year": 1937}
    url = config.get_api_url()
    resp = client.post(f"{url}/books", json=data)
    assert resp.status_code == 201

def test_post_book_returns_201(client):
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