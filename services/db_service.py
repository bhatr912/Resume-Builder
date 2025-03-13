from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from config import MONGODB_URI, DB_NAME

# Global database client
client = None
db = None

def init_db():
    """Initialize the database connection"""
    global client, db
    
    if client is not None:
        return db
    
    client = MongoClient(MONGODB_URI)
    
    try:
        # The ismaster command is cheap and does not require auth
        client.admin.command('ismaster')
        print("MongoDB connection successful")
        db = client.get_database(DB_NAME)
        return db
    except ConnectionFailure:
        print("MongoDB connection failed")
        db = None
        return None

def get_db():
    """Get the database instance"""
    global db
    if db is None:
        return init_db()
    return db

def get_collection(collection_name):
    """Get a collection from the database"""
    database = get_db()
    if database is None:
        return None
    return database[collection_name]

def db_status():
    """Check database connection status"""
    database = get_db()
    if database is None:
        return {"status": "disconnected"}
    return {"status": "connected", "database": DB_NAME}
