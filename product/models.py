from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    cost = models.IntegerField()
    price = models.IntegerField()

    def __str__(self):
        return self.name