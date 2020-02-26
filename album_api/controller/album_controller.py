from flask_restful import Resource
from album_api.dao.album_dao import AlbumDao

dao = AlbumDao


class AlbumApi(Resource):

    @staticmethod
    def get(id_album=None):
        if id_album:
            return dao.get_by_id(id_album=id_album)
        else:
            return dao.list_all_albuns()

    @staticmethod
    def post():
        return dao.add_album()

    @staticmethod
    def put():
        return dao.update_album()

    @staticmethod
    def delete(id_album):
        return dao.delete_album(id_album)
