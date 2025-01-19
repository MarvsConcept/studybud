from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='home',),
    path('room/<str:pk>/', views.room, name='room'),
    path('create-room/', views.createRoom, name='create-room'),
    path('room/<str:pk>/update/', views.updateRoom, name='update-room'),
]
