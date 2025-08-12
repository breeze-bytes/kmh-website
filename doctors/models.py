from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Doctor(models.Model):
    name = models.CharField(max_length=200)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='doctors')
    qualification = models.CharField(max_length=200)
    experience_years = models.PositiveIntegerField()
    specialization = models.CharField(max_length=200)
    consultation_hours = models.CharField(max_length=100, blank=True)
    photo = models.ImageField(upload_to='doctors_photos/', blank=True, null=True)

    def __str__(self):
        return self.name
