from django.urls import path
from . import views

urlpatterns = [
    path('', views.penfriends), #GET request to display home page
]