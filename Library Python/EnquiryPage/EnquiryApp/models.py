from django.db import models

# Create your models here.

class EnquiryData(models.Model):
    name = models.CharField(max_length=50)
    contact = models.IntegerField()
    email = models.EmailField()
    course = models.CharField(max_length=50)


class Trainer(models.Model):
    name = models.CharField(max_length=50)
    contact = models.IntegerField()
    email = models.EmailField()
    course = models.CharField(max_length=50)
    salary = models.FloatField()
    timing = models.CharField(max_length=50)
    today =  models.BooleanField()

