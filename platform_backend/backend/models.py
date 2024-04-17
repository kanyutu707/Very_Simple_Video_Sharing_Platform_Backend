from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Product(models.Model):
    product_name=models.CharField(max_length=255)
    product_price=models.CharField(max_length=255)
    age=models.IntegerField()
    role=models.CharField(max_length=255)
    user=models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    
    def __str__(self):
        return self.product_name
    
class SystemUser(models.Model):
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    age=models.IntegerField()
    email=models.EmailField(max_length=255)
    password=models.CharField(max_length=255)

    def __str__(self):
        return self.first_name