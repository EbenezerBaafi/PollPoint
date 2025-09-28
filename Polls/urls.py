from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), # localhost:8000/polls/ will be routed to views.index
]