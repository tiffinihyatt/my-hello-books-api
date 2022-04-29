
from flask import Blueprint, jsonify, abort, make_response

class Book:
    def __init__(self, id, title, description):
        self.id = id
        self.title = title
        self.description = description

books = [
    Book(1, "How the Word is Passed", "An honest, damning exploration of "
    "plantations throughout the American South and the stories they hold, "
    "from poet and former teacher Clint Smith III."),
    Book(2, "The Misadventures of Awkward Black Girl", "A witty, charming mix "
    "of memoir and short story that guides us through Issa Rae's adolescence "
    "and young adulthood."),
    Book(3, "The Prophets", "Robert Jones Jr.'s gorgeous debut novel that is "
    "equal parts love story, historical fiction, and tragedy.")
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