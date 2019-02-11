from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=50, null=False)
    surname = models.CharField(max_length=50, null=False)
    age = models.IntegerField(null=False)



