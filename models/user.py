from datetime import datetime, UTC
from bson import ObjectId

class User:
    def __init__(self, email, display_name, photo_url, uid, created_at=None, _id=None):
        self.email = email
        self.display_name = display_name
        self.photo_url = photo_url
        self.uid = uid
        self.created_at = created_at or datetime.now(UTC)
        self._id = _id

    @classmethod
    def from_dict(cls, data):
        return cls(
            email=data.get('email'),
            display_name=data.get('displayName'),
            photo_url=data.get('photoURL'),
            uid=data.get('uid'),
            created_at=data.get('createdAt'),
            _id=data.get('_id')
        )

    def to_dict(self):
        return {
            "email": self.email,
            "displayName": self.display_name,
            "photoURL": self.photo_url,
            "uid": self.uid,
            "createdAt": self.created_at
        }

    def to_json(self):
        data = self.to_dict()
        if self._id:
            data['id'] = str(self._id)
        return data
