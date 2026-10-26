"""Part 2: tests against JSONPlaceholder, a public API.

Complete API_FINDINGS.md before writing any test in this file. Each
assertion below should state what you recorded there, not a value
copied from the documentation.

Run with:
    pytest test_public_api.py -v
"""
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


def test_get_single_post():
    """GET /posts/1.

    Assert the status code, the Content-Type header, and that the
    response body contains the keys recorded in API_FINDINGS.md, each
    of the correct type.
    """
    response = requests.get(f"{BASE_URL}/posts/1")

    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json; charset=utf-8"

    data = response.json()

    assert isinstance(data, dict)
    assert "userId" in data
    assert "id" in data
    assert "title" in data
    assert "body" in data

    assert isinstance(data["userId"], int)
    assert isinstance(data["id"], int)
    assert isinstance(data["title"], str)
    assert isinstance(data["body"], str)


def test_get_all_posts():
    """GET /posts.

    Assert the status code, the Content-Type header, and that the
    response body has the shape recorded in API_FINDINGS.md.
    """
    response = requests.get(f"{BASE_URL}/posts")

    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json; charset=utf-8"

    data = response.json()

    assert isinstance(data, list)
    assert len(data) == 100

    first_post = data[0]

    assert isinstance(first_post, dict)
    assert "userId" in first_post
    assert "id" in first_post
    assert "title" in first_post
    assert "body" in first_post

    assert isinstance(first_post["userId"], int)
    assert isinstance(first_post["id"], int)
    assert isinstance(first_post["title"], str)
    assert isinstance(first_post["body"], str)


def test_create_post():
    """POST /posts.

    Send the request body recorded in API_FINDINGS.md. Assert the
    status code, the Content-Type header, and that the response body
    contains the fields you sent, plus the field the server adds.
    """
    payload = {
        "title": "Lab 6 Test",
        "body": "Testing REST API",
        "userId": 1
    }

    response = requests.post(f"{BASE_URL}/posts", json=payload)

    assert response.status_code == 201
    assert response.headers["Content-Type"] == "application/json; charset=utf-8"

    data = response.json()

    assert data["title"] == "Lab 6 Test"
    assert data["body"] == "Testing REST API"
    assert data["userId"] == 1
    assert data["id"] == 101

    assert isinstance(data["title"], str)
    assert isinstance(data["body"], str)
    assert isinstance(data["userId"], int)
    assert isinstance(data["id"], int)


def test_delete_post():
    """DELETE /posts/1.

    Assert the status code and the Content-Type header recorded in
    API_FINDINGS.md.
    """
    response = requests.delete(f"{BASE_URL}/posts/1")

    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json; charset=utf-8"

    assert response.json() == {}