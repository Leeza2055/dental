from django.db import models

# Create your models here.
class Doctor(models.Model):
	name = models.CharField(max_length=100)
	address = models.CharField(max_length=100)
	specialization = models.CharField(max_length=100)
	photo = models.ImageField(upload_to="doctor_photo")
	certificate = models.ImageField(upload_to="doctor_certificate")
	detail = models.TextField()