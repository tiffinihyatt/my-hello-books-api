def test_get_all_books_with_empty_db(client):
    # act
    response = client.get("/books")
    response_body = response.get_json()

    # assert
    assert response.status_code == 200
    assert response_body == []