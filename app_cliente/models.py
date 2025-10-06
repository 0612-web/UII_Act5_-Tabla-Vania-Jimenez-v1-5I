from django.db import models

# Create your models here.

# clase Cliente con campos nombre edad y email
class Cliente(models.Model):
    nombre= models.CharField(max_length=100)
    edad = models.IntegerField()
    email = models.EmailField(unique=True)