from django.db import models

class ContactInfo(models.Model):
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    whatsapp = models.CharField(max_length=20, help_text="WhatsApp number with country code, e.g., 254700123456")
    address = models.CharField(max_length=255)
    map_embed_url = models.TextField(help_text="Google Maps embed iframe URL")
    operating_hours = models.TextField(help_text="e.g., Mon-Fri: 8am - 6pm")
    emergency_contact = models.CharField(max_length=100)

    def __str__(self):
        return f"Contact Info - {self.address}"
