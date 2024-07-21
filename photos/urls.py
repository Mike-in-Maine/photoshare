from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('gallery', views.gallery, name='gallery'),
    path('photo/<str:pk>/', views.viewPhoto, name='photo'),
    path('add', views.addPhoto, name='add'),
    path('importAlbum', views.importAlbum, name='importAlbum'),
    path('index_flo', views.index_flo, name='index_flo'),

]