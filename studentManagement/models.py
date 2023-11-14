from django.db import models


# Create your models here.
class Student(models.Model):
    """
    Classe responsável pelo cadastro de alunos
    """
    nome = models.CharField(max_length=50, blank=False)
    matricula = models.CharField(max_length=11, blank=False)
    sexo = models.CharField(max_length=9, blank=False, choices=[("Masculino", "Masculino"), ("Feminino", "Feminino")])
    curso = models.CharField(max_length=50, blank=False, choices=[("Ads", "Ads" ), ("Eng.Civil", "Eng.civil"), ("Medicina", "Medicina"), ("História", "História"), ("Eng. Aeroespacial", "Eng. Aeroespacial")])
    periodo = models.CharField(max_length=8, blank=False, choices=[("1º", "1º"), ("2º", "2º"), ("3º", "3º"), ("4º", "4º"), ("5º", "5º"), ("6º", "6º"), ("7º", "7º"), ("8º", "8º")])



