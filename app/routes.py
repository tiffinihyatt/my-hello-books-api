from app import db
from app.models.book import Book
from flask import Blueprint, jsonify, make_response, request

books_bp = Blueprint("books_bp", __name__, url_prefix="/books")

@books_bp.route("", methods=["POST"])
def create_book():
    request_body = request.get_json()
    new_book = Book(title=request_body["title"],
                    description=request_body["description"])

    db.session.add(new_book)
    db.session.commit()

    return make_response(f"Book {new_book.title} successfully created", 201)

@books_bp.route("", methods=["GET"])
def read_all_books():
    books_response = []
    books = Book.query.all()
    for book in books:
        books_response.append(
            {
                "id": book.id,
                "title": book.title,
                "description": book.description
            }
        )
    return jsonify(books_response)

@books_bp.route("/<book_id>", methods=["GET"])
def get_book_by_id(book_id):
    book = Book.query.get(book_id)

    return {
        "id": book.id,
        "title": book.title,
        "description": book.description
    }

#def validate_book(book_id):
#    try:
#        book_id = int(book_id)
#    except:
#        abort(make_response({"message":f"book {book_id} invalid"}, 400))
#
#    for book in books:
#        if book.id == book_id:
#            return book
#
#    abort(make_response({"message":f"book {book_id} not found"}, 404))
        
# @books_bp.route("/<book_id>", methods=["GET"])
# def handle_book(book_id):
#     book = validate_book(book_id)
#
#     return {
#           "id": book.id,
#           "title": book.title,
#           "description": book.description,
#     }


