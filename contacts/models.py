from django.db import models

class ContactInfo(models.Model):
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    whatsapp_link = models.URLField(blank=True, null=True)
    operating_hours = models.TextField()
    emergency_contacts = models.TextField()
    map_embed_url = models.URLField(
        help_text="Paste your Google Maps embed link here"
    )

    def __str__(self):
        return f"Contact Info ({self.phone})"
