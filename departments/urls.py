from django.urls import path
from .views import departments_view

urlpatterns = [
    path('', departments_view, name='departments'),
]
