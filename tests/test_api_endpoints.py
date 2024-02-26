# test_api_endpoints.py
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_and_delete_contact():
    # create a contact
    response = client.post(
        "/contacts/",
        json={"name": "John Doe", "email": "john.doe@example.com", "message": "Hello, World!"}
    )
    assert response.status_code == 200
    contact_id = response.json()["id"]
    assert response.json()["email"] == "john.doe@example.com"

    # delete the contact
    delete_response = client.delete(f"/contacts/{contact_id}")
    assert delete_response.status_code == 200
    assert delete_response.json() == {"message": "Contact deleted successfully"}
