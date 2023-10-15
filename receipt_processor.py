import json
from flask import Flask, request, jsonify
import hashlib
import math
from datetime import datetime

app = Flask("receipt-processor")

#Using in memory storage to store the receipt id and receipt json.
receipts_data = {}

"""
Submits a request for processing 
Path:/receipts/process
Request Type: Post
contentType : "application/json"
Output:"application/json"
Description: Takes the input as a json. Generates a hash code using the receipt data, calculates the points based on the rules provided. And return the unique ID to the user.
Reference: https://datagy.io/python-sha256/
Response Status: 200 Success
400: Invalid JSON
500: Invalid request
Assumption: Same receipt json generate same unique id(same hash)
"""
@app.route('/receipts/process', methods = ['POST'])
def process_receipt():
    try:
        if request.is_json:
            #Getting the request json and storing it in a variable.
            receipt_json = request.get_json()
            #reference https://datagy.io/python-sha256/ to generate a unique hash code for each json
            unique_receipt_id = hashlib.sha256(json.dumps(receipt_json).encode('utf-8')).hexdigest()
            if unique_receipt_id not in receipts_data:
                points = calculate_points(receipt_json)
                receipt_json["points"] = points
                receipts_data[unique_receipt_id] = receipt_json
            response = {"id":unique_receipt_id}
            #Success status is 200
            return jsonify(response), 200
        else:
            #Invalid request status: 400.
            return "The JSON you provided was invalid", 400 

    except Exception as e:
        return str(e), 500
        #return "Invalid request, please check the request", 500


"""
Submits a request for processing 
Path:receipt/{id}/points
Request Type: GET
Output:"application/json"
Description: Takes the integer a json. Generates a hash code using the receipt data, calculates the points based on the rules provided. And return the unique ID to the user.
Reference: https://datagy.io/python-sha256/
Response Status: 200 Success
400: Invalid JSON
500: Invalid request
Assumption: Same receipt json generate same unique id(same hash)
"""
@app.route('/receipts/<string:id>/points', methods = ['GET'])
def get_receipt_points(id):
    try:
        if id in receipts_data:
            receipt_details = receipts_data[id]
            points = receipt_details["points"]
            response = {"points": points}
            return jsonify(response), 200  # 200 Status ok
        else:
            return "Receipt not found. Please try again with a different receipt id", 404
    except:
        return "Invalid request, please check the request", 500


def calculate_points(receipt):
    points = 0

    # Rule 1: One point for every alphanumeric character in the retailer name
    retailer_name = receipt.get('retailer', '')
    points += sum(1 for char in retailer_name if char.isalnum())

    # Rule 2: 50 points if the total is a round dollar amount with no cents
    total = float(receipt.get('total', 0))
    if total.is_integer():
        points += 50

    # Rule 3: 25 points if the total is a multiple of 0.25
    if total % 0.25 == 0:
        points += 25
    # Rule 4: 5 points for every two items on the receipt
    items = receipt.get('items', [])
    points += (len(items) // 2) * 5

    # Rule 5: If the trimmed length of the item description is a multiple of 3,
    # multiply the price by 0.2 and round up to the nearest integer.
    for item in items:
        description_length = len(item.get('shortDescription', '').strip())
        if description_length % 3 == 0:
            price = float(item.get('price', 0))
            points += math.ceil(price * 0.2)

    # Rule 6: 6 points if the day in the purchase date is odd
    purchase_date = receipt.get('purchaseDate', '')
    day = int(purchase_date.split('-')[2])  # Assume date format is YYYY-MM-DD
    if day % 2 == 1:
        points += 6

    # Rule 7: 10 points if the time of purchase is after 2:00pm and before 4:00pm
    purchase_time = receipt.get('purchaseTime', '')
    hour = int(purchase_time.split(':')[0])  # Assume time format is HH:MM:SS
    if 14 <= hour < 16:
        points += 10

    return points


if __name__ == '__main__':
    app.run(debug=True)