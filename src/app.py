"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure
# from models import Person


app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# Create the jackson family object
jackson_family = FamilyStructure("Jackson")


# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code


# Generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)


# GET all the members of the family

@app.route('/members', methods=['GET'])
def get_all_members():
    members = jackson_family.get_all_members()
    return jsonify(members), 200

# GET a member by ID, remember we use <int:member_id> to indicate the end of the route witch contains the id as a parameter.
# Also the function get_one_member call the method get_member

@app.route('/members/<int:member_id>', methods=['GET'])
def get_one_member(member_id):
    member = jackson_family.get_member(member_id)
    if member is None:
        return jsonify({"error": "Member not found"}), 404
    print(member)

    return jsonify({
        "id": member["id"],
        "first_name": member["first_name"],
        "age": member["age"],
        "lucky_numbers": member["lucky_numbers"]
    }), 200


# POST / add a member.

@app.route('/members', methods=['POST'])
def add_new_member():
    # Similar to a promise declaration we use the method try in POST method
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "Missing JSON body"}), 400
        
        # Basic validation last name always by a default value, but in other cases name. age and lucky are "inputs" in the API
        if "first_name" not in data or "age" not in data or "lucky_numbers" not in data:
            return jsonify({"error": "Missing required fields"}), 400
        
        # We call the method of the datastructure in this line and return the resolve promise jsonify. Important for the post method
        add_new_member = jackson_family.add_member(data)
        return jsonify(add_new_member), 200
    
# This allow us to "catch" the error during the request 
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# DELETE method.

@app.route('/members/<int:member_id>', methods=['DELETE'])
def delete_member(member_id):
    member = jackson_family.get_member(member_id)
    if member:
        jackson_family.delete_member(member_id)
        return jsonify({"done": True}), 200
    else:
        return jsonify({"error": "Member not found"}), 404

# This only runs if `$ python src/app.py` is executed. For this reason when we write in the terminar this command the server turn on
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
