from django.shortcuts import render

def index(request):
    return render(request, 'gallery/gallery.html')  # Make sure template exists
