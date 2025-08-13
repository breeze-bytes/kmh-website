from django.shortcuts import render
from .models import ContactInfo

def contact_view(request):
    contact_info = ContactInfo.objects.first()
    return render(request, 'contacts/contact.html')
