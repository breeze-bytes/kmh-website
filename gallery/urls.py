from django.urls import path
from . import views  # Import the views module

urlpatterns = [
    path('', views.index, name='gallery'),  # Match the view function in views.py
]
