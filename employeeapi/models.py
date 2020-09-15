from django.db import models

# Create your models here.

class Employee(models.Model):
    fullname = models.CharField(max_length=100)
    emp_code = models.CharField(max_length=3)
    mobile = models.CharField(max_length=15)


class Notes(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)


class User(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    password = models.CharField(max_length=30)


    # Create / Insert / Add - POST
    # Retrieve /  Fetch - GET
    # Update / Edit - PUT
    # Delete / Remove - DELETE