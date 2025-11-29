from django.db import models

# Create your models here.
class newone(models.Model):
    movie_name = models.CharField(max_length=100,unique=True)
    ral_date = models.CharField(max_length=100)
    budget = models.CharField(max_length=100)
    rating = models.IntegerField()

class idea(models.Model):
    nameuser = models.CharField(max_length=100,unique=True)
    phonenumber = models.IntegerField()
    address = models.CharField(max_length=100)
