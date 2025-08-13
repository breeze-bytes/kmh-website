from django.urls import path
from . import views  # import your views.py from departments app

urlpatterns = [
    path('', views.departments_view, name='departments'),
]
