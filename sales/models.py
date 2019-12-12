from django.db import models

from customer.models import Customer
from product.models import Product


class Payment(models.Model):
    division = models.CharField(max_length=255)


class Sales(models.Model):
    sales_date = models.DateField()
    customer = models.ForeignKey(Customer, related_name='customer', on_delete=models.PROTECT)
    total = models.IntegerField()
    payment = models.ForeignKey(Payment, on_delete=models.PROTECT)

    def __str__(self):
        return str(self.sales_date) + ' ' + self.customer.name


class SalesDetail(models.Model):
    sales = models.ForeignKey(Sales, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='product', on_delete=models.PROTECT)
    price = models.IntegerField()
    amount = models.IntegerField()
    sub_total = models.IntegerField()
