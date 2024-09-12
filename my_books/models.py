from django.db import models

class Kitob(models.Model):
    nom = models.CharField(max_length=200)  # Kitob nomi
    muallif = models.CharField(max_length=100)  # Muallif ismi
    nashr_sana = models.DateField()  # Nashr etilgan sana
    isbn = models.CharField(max_length=13, unique=True)  # ISBN raqami
    sahifalar_soni = models.IntegerField()  # Kitobning sahifalar soni
    til = models.CharField(max_length=30)  # Kitob tili
    janr = models.CharField(max_length=50)  # Kitob janri
    def __str__(self):
        return self.title
