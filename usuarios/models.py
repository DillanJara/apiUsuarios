from django.db import models

# Create your models here.
class Usuario(models.Model):
    idUsuario=models.AutoField(primary_key=True)
    nombreUsuario=models.CharField(max_length=50)
    correoUsuario=models.CharField(max_length=50)
    claveUsuario=models.CharField(max_length=50)

