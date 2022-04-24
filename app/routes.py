
from flask import Blueprint, jsonify

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

books_bp = Blueprint("books_bp", __name__, url_prefix="/books")

@books_bp.route("", methods=["GET"])
def handle_books():
    # convert lines 26-34 to list comprehension
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