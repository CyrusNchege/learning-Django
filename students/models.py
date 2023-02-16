from django.db import models

# Create your models here.
class student (models.Model):
    studentname= models.CharField(max_length=250)
    studentage=models.CharField(max_length=100)
    department=models.CharField(max_length=250)
    studentmajor=models.CharField(max_length=100, default='undeclared')
    campus=models.CharField(max_length=100, null=True)


def __str__(self):
    return self.title