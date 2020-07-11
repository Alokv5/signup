from django.db import models
import datetime

# Create your models here.
class Employee(models.Model):
    emp_id=models.AutoField(primary_key=True)
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    password = models.CharField(max_length=100, default=not None)
    contact = models.CharField(max_length=20, default=not None)

    def __str__(self):
        return self.first_name




