from django.db import models

class Dish(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    items=models.TextField()
    latitude=models.FloatField()
    longitude = models.FloatField() 
    full_details=models.TextField()
    def __str__(self):
        return str(self.id)+" "+self.name+" "+self.location


# Create your models here.# mainApp/models.py
