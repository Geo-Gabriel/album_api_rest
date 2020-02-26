from flask_restful import Resource
from album_api.dao.photo_dao import PhotoDao


dao = PhotoDao


class PhotoApi(Resource):

    @staticmethod
    def get(id_photo=None):
        if id_photo:
            return dao.get_by_id(id_photo=id_photo)
        else:
            return dao.list_all_photos()

    @staticmethod
    def post():
        return dao.add_photo()

    @staticmethod
    def put():
        return dao.update_photo()

    @staticmethod
    def delete(id_photo):
        return dao.delete_photo(id_photo)
