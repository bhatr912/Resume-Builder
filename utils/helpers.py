import json
from bson import ObjectId

class JSONEncoder(json.JSONEncoder):
    """Custom JSON encoder that can handle MongoDB ObjectId"""
    def default(self, obj):
        if isinstance(obj, ObjectId):
            return str(obj)
        return super(JSONEncoder, self).default(obj)

def json_response(data):
    """Convert data to JSON response with proper handling of MongoDB ObjectId"""
    return json.dumps(data, cls=JSONEncoder)
