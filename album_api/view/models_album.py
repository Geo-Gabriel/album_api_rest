
from album_api import db

class Album(db.Model):
    __tablename__ = 'album'

    id_album = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(255), nullable=False)
    public = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, nullable=False)



class Photo(db.Model):
    __tablename__ = 'photos'

    id_photo = db.Column(db.Integer, primary_key=True)
    link = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    principal = db.Column(db.Integer, nullable=False)
    album_id = db.Column(db.ForeignKey('album.id_album'), nullable=False, index=True)

    album = db.relationship('Album', primaryjoin='Photo.album_id == Album.id_album', backref='photos')

# db.create_all()