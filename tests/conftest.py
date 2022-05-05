import pytest
from app import create_app
from app import db
from app.models.book import Book
from flask.signals import request_finished


@pytest.fixture
def app():
    app = create_app({"TESTING": True})

    @request_finished.connect_via(app)
    def expire_session(sender, response, **extra):
        db.session.remove()

    with app.app_context():
        db.create_all()
        yield app

    with app.app_context():
        db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def two_books(app):
    book1 = Book(id=1, title="Americanah", description="YA fiction")
    book2 = Book(id=2, title="The Notebook", description="Historical romance")

    db.session.add(book1)
    db.session.add(book2)
    db.session.commit()