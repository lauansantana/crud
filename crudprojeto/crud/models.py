from django.db import models

# Create your models here.

class Estudante(models.Model):
    matricula=models.CharField(max_length=12)
    nome=models.CharField(max_length=70)
    email=models.CharField(max_length=100)
    endereco=models.CharField(max_length=150)
    telefone=models.CharField(max_length=11)