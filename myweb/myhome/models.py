from django.db import models

# Create your models here.
class Citys(models.Model):
    name=models.CharField(max_length=50)
    upid=models.IntegerField()

    class Meta():
        db_table='district'