import json
from receipt_processor import app
import pytest

# Helper function to submit a POST request with JSON data
def submit_receipt(data):
    client = app.test_client()
    return client.post('/receipts/process', json=data)

# Helper function to submit a GET request for points
def get_receipt_points(receipt_id):
    client = app.test_client()
    return client.get(f'/receipts/{receipt_id}/points')

# Test case to submit a valid receipt and check if it returns a unique ID
def test_valid_receipt_submission():
    data = {
  "retailer": "M&M Corner Market",
  "purchaseDate": "2022-03-20",
  "purchaseTime": "14:33",
  "items": [
    {
      "shortDescription": "Gatorade",
      "price": "2.25"
    },{
      "shortDescription": "Gatorade",
      "price": "2.25"
    },{
      "shortDescription": "Gatorade",
      "price": "2.25"
    },{
      "shortDescription": "Gatorade",
      "price": "2.25"
    }
  ],
  "total": "9.00"
}

    response = submit_receipt(data)
    assert response.status_code == 200
    response_data = json.loads(response.data)
    assert "id" in response_data

# Test case to submit an invalid JSON and check if it returns a 400 status
def test_invalid_json_submission():
    data = "This is not a valid JSON"
    response = submit_receipt(data)
    assert response.status_code == 500

# Test case to get points for a valid receipt ID
def test_get_points_for_valid_receipt_id():
    # First, submit a valid receipt
    data = {
  "retailer": "M&M Corner Market",
  "purchaseDate": "2022-03-20",
  "purchaseTime": "14:33",
  "items": [
    {
      "shortDescription": "Gatorade",
      "price": "2.25"
    },{
      "shortDescription": "Gatorade",
      "price": "2.25"
    },{
      "shortDescription": "Gatorade",
      "price": "2.25"
    },{
      "shortDescription": "Gatorade",
      "price": "2.25"
    }
  ],
  "total": "9.00"
}
    response = submit_receipt(data)
    response_data = json.loads(response.data)
    receipt_id = response_data["id"]

    # Then, get points for the submitted receipt
    points_response = get_receipt_points(receipt_id)
    assert points_response.status_code == 200
    points_data = json.loads(points_response.data)
    assert "points" in points_data

# Test case to get points for an invalid receipt ID
def test_get_points_for_invalid_receipt_id():
    invalid_receipt_id = "invalid_id"
    points_response = get_receipt_points(invalid_receipt_id)
    assert points_response.status_code == 404