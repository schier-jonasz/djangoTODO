from django.contrib import admin
from django.urls import path, include
from .views import *

app_name = 'app'
urlpatterns = [
    path('', index, name = "index"),
    path('update_task/<str:pk>/', updateTask, name = "updateTask"),
    path('delete_task/<str:pk>/', deleteTask, name = "deleteTask"),
]