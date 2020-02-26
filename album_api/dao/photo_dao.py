from album_api import db
from album_api.model.photo_model import Photo
from flask import request


class PhotoDao:

    @staticmethod
    def add_photo():
        try:
            link = request.json['link']
            description = request.json['description']
            principal = request. json['principal']
            album_id = request.json['album_id']
            new_photo = Photo(link=link, description=description, principal=principal, album_id=album_id)
            db.session.add(new_photo)
            db.session.commit()
            return {"message": "success when inserting a new photo"}

        except:
            return {"message": "failed when inserting photo, please try again and verify your data are correct"}

    @staticmethod
    def list_all_photos():
        all_photos = db.session.query(Photo).all()
        return [photo.serialize() for photo in all_photos]

    @staticmethod
    def get_by_id(id_photo):
        try:
            photo = db.session.query(Photo).filter_by(id_photo=id_photo).first()
            return photo.serialize()

        except:
            return {"message": "Error when searching photo by id or does not exist"}

    @staticmethod
    def update_photo():
        try:
            link = request.json['link']
            description = request.json['description']
            principal = request.json['principal']
            album_id = request.json['album_id']
            new_photo = Photo(link=link, description=description, principal=principal, album_id=album_id)
            db.session.merge(new_photo)
            db.session.commit()
            return {"message": "Success when updating photo"}

        except:
            return {"message": "Failed when updating photo"}

    @staticmethod
    def delete_photo(id_photo):
        try:
            photo = db.session.query(Photo).filter_by(id_photo=id_photo().first())
            db.session.delete(photo)
            db.session.commit()
            return {"message": "photo deleted"}

        except:
            return {"message": "Failed when deleting photo"}
