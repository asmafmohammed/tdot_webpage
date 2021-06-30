from django.db import models

class Ranking(models.Model):
    City = models.CharField(primary_key=True, max_length=50)
    County = models.CharField(max_length=50) 
    Zip = models.IntegerField()
    Intersection = models.CharField(max_length=200)
    Ranking = models.IntegerField()
    class Meta:
        db_table="dummy"