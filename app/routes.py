
from flask import Blueprint, jsonify, abort, make_response

class Book:
    def __init__(self, id, title, description):
        self.id = id
        self.title = title
        self.description = description

books = [
    Book(1, "Fictional Book", "A fantasy novel set in an imaginary world."),
    Book(2, "Wheel of Time", "A fantasy novel set in an imaginary world."),
    Book(3, "Fictional Book Title", "A fantasy novel set in an imaginary world.")
]

def validate_book(book_id):
    # try/except to confirm that book_id is numeric
    try:
        book_id = int(book_id)
    except:
        abort(make_response({"message":f"book {book_id} invalid"}, 400))
    
    for book in books:
        if book.id == book_id:
            return book
    
    abort(make_response({"message":f"book {book_id} not found"}, 404))

books_bp = Blueprint("books_bp", __name__, url_prefix="/books")

@books_bp.route("", methods=["GET"])
def handle_books():
    books_response = []
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
def handle_single_book(book_id):
    book = validate_book(book_id)
    
    return {
        "id": book.id,
        "title": book.title,
        "description": book.description,
    }