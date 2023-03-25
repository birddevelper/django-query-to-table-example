from django.db import models

class Order(models.Model):
    order_number = models.IntegerField()
    order_item = models.TextField()
    customer_name = models.CharField(max_length=50)
    order_date = models.DateField()
    total_amount = models.DecimalField(max_digits=8, decimal_places=2)
