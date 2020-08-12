from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(null=True, auto_now_add=True)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    choices = [
        ('Indoor', 'Indoor'),
        ('Out Door', 'Out Door'),
    ]

    tag = models.ManyToManyField(Tag)
    name = models.CharField(max_length=200, null=True)
    price = models.FloatField()
    category = models.CharField(max_length=200, null=True, choices=choices)
    description = models.CharField(max_length=200, null=True, blank=True)
    date_created = models.DateTimeField(null=True, auto_now_add=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    status = [
        ('Pending', 'Pending'),
        ('Out for delivery', 'Out for delivery'),
        ('Delivered', 'Delivered'),
    ]

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    status = models.CharField(max_length=200, null=True, choices=status)
    note = models.CharField(max_length=200, null=True, blank=True)
    date_created = models.DateTimeField(null=True, auto_now_add=True)
