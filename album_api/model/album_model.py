from album_api import db
from album_api.model.photo_model import Photo

class Album(db.Model):

    __tablename__ = 'album'

    id_album = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(255), nullable=False)
    public = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, nullable=False)

    def __init__(self, description, public, user_id, id_album=None):

        self.id_album = id_album
        self.description = description
        self.public = public
        self.user_id = user_id

    def serialize(self):

        return {
            "id_album": self.id_album,
            "description": self.description,
            "public": self.public,
            "user_id": self.user_id,
        }
