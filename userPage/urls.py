from django.urls import path
from . import views

url_patterns = [
    path("<int:id>", views.userPage_view, name='userPage')
]