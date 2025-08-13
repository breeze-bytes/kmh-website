from django.shortcuts import render


def contact(request):
    contact_info = {
        "phone": "0102186778",
        "email": "kmedh2014@gmail.com",
        "whatsapp": "254102186778",  # WhatsApp requires country code
        "address": "P.O. Box 376, Code 01-020 Kenol",
        "operating_hours": "Mon - Fri: 8:00 AM - 5:00 PM, Sat: 9:00 AM - 1:00 PM",
        "emergency_contact": "0102186778",  # same as phone
    }
    return render(request, "contacts/contact.html")
