from django.shortcuts import render
from .models import Department

def doctors_view(request):
    departments = Department.objects.prefetch_related('doctors').all()
    return render(request, 'doctors/doctors.html', {'departments': departments})
