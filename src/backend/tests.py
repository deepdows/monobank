from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_cards():
    # valid request main endpoint
    response = client.get("/cards/")
    assert response.status_code == 200

    for object in response.json():
        assert object['currency'] == 'USD'

    # invalid request main endpoint
    invalid_response = client.get("/cards/")
    assert invalid_response.status_code == 400
    assert invalid_response.json() == {"detail": "notCurrency - is not currency"}

def test_login_template():
    pass