from django.db import models

# Create your models here.


# class Person(models.Model):
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=30)#FloatField
    
class Car(models.Model):
    marka = models.CharField(max_length=100)
    color = models.CharField(max_length=50)
    volume = models.IntegerField()
    power = models.FloatField()
    
    def __str__(self):
        return f'{self.marka}-{self.color}'