from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=255)
    tel = models.CharField(max_length=11, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)
    postal_code = models.CharField(max_length=7, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)