from django.db import models
from django.utils import timezone

class Department(models.Model):
    # You can reuse the Department from doctors app or redefine here
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Appointment(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    reason = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    confirmed = models.BooleanField(default=False)  # For future use

    def __str__(self):
        return f"{self.name} - {self.department.name} on {self.date} at {self.time}"
