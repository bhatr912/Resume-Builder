from flask import request, jsonify
from services.db_service import get_collection
from models.user import User
from datetime import datetime, UTC

def register_user_routes(app):
    @app.route('/save-user', methods=['POST'])
    def save_user():
        users_collection = get_collection('Users')
        if users_collection is None:
            return jsonify({"error": "Database connection failed"}), 500
        
        data = request.json
        user = User.from_dict(data)
        
        try:
            # Check if user already exists
            existing_user = users_collection.find_one({"uid": user.uid})
            if existing_user:
                return jsonify({"message": "User already exists"}), 200
            
            # Insert new user
            result = users_collection.insert_one(user.to_dict())
            return jsonify({
                "message": "User saved successfully",
                "userId": str(result.inserted_id)
            }), 201
            
        except Exception as e:
            return jsonify({"error": str(e)}), 500
