from django.db import models

class UserModel(models.Model):
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    username = models.CharField(max_length=200, unique=True)
    address = models.CharField(max_length=200, null=True)

class PoductModel(models.Model):
    ProductName = models.CharField(max_length=200)
    ProductDescription = models.CharField(max_length=200)
    ProductImage = models.ImageField(upload_to='photos/', null=True, max_length=254)
    ProductPrice = models.DecimalField(max_digits=10, decimal_places=2)