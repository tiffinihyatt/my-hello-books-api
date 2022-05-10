from app import db
from app.models.author import Author
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