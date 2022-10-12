import pytest

from app import app

@pytest.fixture
def client():
    client = app.test_client()
    return client


def test_root(client):
    """Test the default route."""

    res = client.get("/")
    assert b"Hello world!" in res.data


def test_json(client):
    """Test the json route."""

    res = client.get("/json")
    assert res.status_code == 200
    assert b"hostname" in res.data
    assert b"mimetype" in res.data
    assert b"name" in res.data
    assert b"python_version" in res.data
    assert b"user" in res.data
