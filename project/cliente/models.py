from django.db import models

# Create your models here.
class Pais(models.Model):
    name = models.CharField(max_length=100, unique=True)
    def __str__(self):
        return self.name


class Cliente(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    country = models.ForeignKey(Pais, on_delete=models.SET_NULL, null=True, blank=True)
    nacimiento = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} {self.last_name} {self.nacimiento}"
        