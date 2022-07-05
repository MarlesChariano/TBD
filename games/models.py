from django.db import models

class Games(models.Model):
    titulo = models.CharField(primary_key=True,max_length=50)
    genero = models.CharField(max_length=10,default='None')
    anolanzamiento = models.IntegerField(default=0000)