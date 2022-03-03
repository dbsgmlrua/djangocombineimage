from django.urls import path
from . import views
from .views import Test, gomimg, img, enumTest, makeImageAndData, getmetadatatojson, metadata, getmetadata, getmetadatabyid

urlpatterns = [
    path('test', Test),
    path('image/<int:body>/<int:hat>/<int:weapon>', img),
    path('imagenew/<int:bg>/<int:gom>/<int:eye>/<int:mouth>/<int:hat>/<int:hand>', gomimg),
    path('enum/<int:number>', enumTest),
    path('combine', makeImageAndData),
    path('metadata', metadata),
    path('getmetadata', getmetadata),
    path('getmetadatajson', getmetadatatojson),
    path('getmetadata/<int:id>', getmetadatabyid)
]