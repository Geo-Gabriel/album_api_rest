from album_api import api
from album_api.controller.album_controller import AlbumApi
from album_api.controller.photo_controller import PhotoApi


api.add_resource(AlbumApi, "/api/album", endpoint="albums")
api.add_resource(AlbumApi, "/api/album/<int:id_album>", endpoint="album")

api.add_resource(PhotoApi, "/api/photo", endpoint="photos")
api.add_resource(PhotoApi, "/api/photo/<int:id_photo>", endpoint="photo")

