import os
import pytest
from flask import Flask
from flask import request
from main import hello_http


@pytest.fixture(scope='session', autouse=True)
def client():
    # setup
    app = Flask(__name__)

    # 間接的にhello_httpを呼び出す
    @app.route("/")
    def _hello_http():
        return hello_http(request)

    client = app.test_client()

    yield client

    # teardown

def test_hello_world(client):
    rv = client.get('/')
    assert b'Hello, World!' in rv.data

def test_hello_yamada(client):
    rv = client.get('/', json={
        'message': 'yamada'
    })
    assert b'Hello, yamada!' in rv.data
