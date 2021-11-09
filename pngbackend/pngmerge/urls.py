from django.urls import path
from . import views
from .views import Test, img

urlpatterns = [
    path('test', Test),
    path('image/<int:body>/<int:hat>/<int:weapon>', img)
]