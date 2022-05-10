from app import db
from app.models.author import Author
from app.models.book import Book
from flask import Blueprint, jsonify, make_response, request, abort

authors_bp = Blueprint("authors_bp", __name__, url_prefix="/authors")

# create new author
@authors_bp.route("", methods=["POST"])
def create_author():
    request_body = request.get_json()
    new_author = Author(name=request_body["name"])

    db.session.add(new_author)
    db.session.commit()

    return make_response(jsonify(f"Author {new_author.name} successfully created", 201))

# create a new book by a specific author
@authors_bp.route("/<author_id>/books", methods=["POST"])
def create_book_with_author(author_id):
    author = validate_author(author_id)
    request_body = request.get_json()

    book = Book(
        title=request_body["title"],
        description=request_body["description"],
        author=author
    )
    
    db.session.add(book)
    db.session.commit()

    return make_response(jsonify(f"Book {book.title} by {author.name} successfully created", 201))

# get all authors
@authors_bp.route("", methods=["GET"])
def get_all_authors():
    authors_response = []
    authors = Author.query.all()

    for author in authors:
        authors_response.append({
            "id": author.id,
            "name": author.name
        })
    
    return jsonify(authors_response)

# get all books by one author
@authors_bp.route("/<author_id>/books", methods=["GET"])
def get_all_books_by_author(author_id):
    author = validate_author(author_id)
    books_response = []

    for book in author.books:
        books_response.append({
            "id": book.id,
            "title": book.title,
            "description": book.description
        })
    
    return jsonify(books_response)

# helper function to validate author
def validate_author(author_id):
    try:
        author_id = int(author_id)
    except:
        abort(make_response({"message":f"Invalid author id"}, 400))

    author = Author.query.get(author_id)

    if not author:
        abort(make_response({"message":f"Author id {author_id} not found"}, 404))
    
    return author