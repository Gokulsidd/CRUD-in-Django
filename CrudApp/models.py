from django.db import models


class Employee(models.Model):
    emp_id = models.IntegerField()
    emp_name = models.CharField(max_length=200)
    emp_age = models.IntegerField()
    emp_pnumber = models.CharField(max_length=10)
