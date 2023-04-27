from django.db import models

class Tickets(models.Model):
    image = models.ImageField(null=True)
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=250)
    location = models.CharField(max_length=100)
    duration = models.CharField(max_length=120)
    date = models.DateTimeField()
    airport = models.CharField(max_length=50)
    extras = models.CharField(max_length=30)
    price = models.IntegerField()

    def __str__(self):
        return self.name

class Contacts(models.Model):
    location = models.CharField(max_length=100)
    home_numb = models.CharField(max_length=100)
    numb_phone= models.CharField(max_length=50)
    data_works = models.CharField(max_length=50)
    email = models.EmailField()

