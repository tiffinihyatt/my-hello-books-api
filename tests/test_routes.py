def test_get_all_books_with_empty_db(client):
    # act
    response = client.get("/books")
    response_body = response.get_json()

    # assert
    assert response.status_code == 200
    assert response_body == []

def test_get_one_book(client, two_books):
    response = client.get("/books/1")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == {
        "id": 1,
        "title": "Americanah",
        "description": "YA fiction"
    }