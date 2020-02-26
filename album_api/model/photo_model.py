from album_api import db


class Photo(db.Model):
    __tablename__ = 'photos'

    id_photo = db.Column(db.Integer, primary_key=True)
    link = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    principal = db.Column(db.Integer, nullable=False)
    album_id = db.Column(db.ForeignKey('album.id_album'), nullable=False, index=True)

    album = db.relationship('Album', primaryjoin='Photo.album_id == Album.id_album', backref='photos')

    def __init__(self, link, description, principal, album_id, id_photo=None):
        self.id_photo = id_photo
        self.link = link
        self.description = description
        self.principal = principal  # -- Accept only -- true or false
        self.album_id = album_id

    def serialize(self):
        return {
            "id_photo": self.id_photo,
            "link": self.link,
            "description": self.description,
            "principal": self.principal,
            "album_id": self.album_id
        }

    def serialize_link(self):
        return {
            "link_photos": self.link
        }
