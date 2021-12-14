from django.urls import path
from . import views
from .views import Test, img, enumTest

urlpatterns = [
    path('test', Test),
    path('image/<int:body>/<int:hat>/<int:weapon>', img),
    path('imagenew/<int:bg>/<int:gom>/<int:eye>/<int:mouth>/<int:head>/<int:hand>', img),
    path('enum/<int:number>', enumTest)
]