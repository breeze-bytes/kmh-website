from django.shortcuts import render, redirect
from .forms import AppointmentForm

def book_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'appointments/confirmation.html', {'name': form.cleaned_data['name']})
    else:
        form = AppointmentForm()
    return render(request, 'appointments/book.html', {'form': form})
