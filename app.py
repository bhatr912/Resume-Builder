from flask import Flask
from flask_cors import CORS
import os
from routes import register_routes
from services.db_service import init_db

def create_app():
    app = Flask(__name__)
    CORS(app)
    
    # Initialize database
    init_db()
    
    # Register all routes
    register_routes(app)
    
    return app

app = create_app()

if __name__ == '__main__':
    from config import PORT, HOST, DEBUG
    app.run(host=HOST, port=PORT, debug=DEBUG)