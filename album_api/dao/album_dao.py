from album_api import db
from album_api.model.album_model import Album
from flask import request


class AlbumDao:

    @staticmethod
    def add_album():
        try:
            description = request.json['description']
            public = request.json['public']
            user_id = request.json['user_id']
            new_album = Album(description=description, public=public, user_id=user_id)
            db.session.add(new_album)
            db.session.commit()
            return {"message": "Success when inserting a new album"}

        except:
            return {"message": "failed when inserting album, please try again and verify your data are correct"}

    @staticmethod
    def list_all_albuns():
        all_albuns = db.session.query(Album).all()
        return [album.serialize() for album in all_albuns]

    @staticmethod
    def get_by_id(id_album):
        try:
            album = db.session.query(Album).filter_by(id_album=id_album).first()
            return album.serialize()

        except AttributeError:
            return {"message": "Error when searching album by id or does not exist"}

    @staticmethod
    def update_album():
        try:
            description = request.json['description']
            public = request.json['public']
            user_id = request.json['user_id']
            new_album = Album(description=description, public=public, user_id=user_id)
            db.session.merge(new_album)
            db.session.commit()
            return {"message": "Success when updating album"}

        except:
            return {"message": "Failed when updating album"}

    @staticmethod
    def delete_album(id_album):
        try:
            album = db.session.query(Album).filter_by(id_album=id_album).first()
            db.session.delete(album)
            db.session.commit()
            return {"message": "Album removed"}
        except:
            return {"message": "Error when deleting album by id or does not exist"}
