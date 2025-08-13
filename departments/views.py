from django.shortcuts import render

def departments_view(request):
    return render(request, 'departments/departments.html')
