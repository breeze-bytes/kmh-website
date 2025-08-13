from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')), 
    path('about/', include('about.urls')),
    path('departments/', include('departments.urls')),
    path('doctors/', include('doctors.urls')),
    path('appointments/', include('appointments.urls')),
    path('contact/', include('contacts.urls')),  # Main contact route
    path('contacts/', RedirectView.as_view(url='/contact/', permanent=True)),  # Redirect old /contacts/ to /contact/
    path('patients-resources/', include('patients_resources.urls')),
    path('gallery/', include('gallery.urls')),
    path('testimonials/', include('testimonials.urls')),
    path('careers/', include('careers.urls')),
]
