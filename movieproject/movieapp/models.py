from django.db import models

# Create your models here.
class Movie(models.Model):
    moviename=models.CharField(max_length=30)
    releasedate=models.DateField()
    heroname=models.CharField(max_length=30)
    heroinename=models.CharField(max_length=30)
    rating=models.IntegerField()
