from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    first_name =  models.CharField(max_length=50)
    last_name =  models.CharField(max_length=50)
    username = models.CharField(max_length=50,unique=True)
    password = models.CharField(max_length=250)
    email = models.EmailField(max_length=254 )
    is_employee = models.BooleanField(default=False)
    position = models.CharField(max_length=100)
    phone_number = models.BigIntegerField(default=0)
    date_of_birth = models.DateField(null=True)
    national_id = models.CharField(max_length=100)

    def __str__(self):
        return self.username