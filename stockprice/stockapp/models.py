from django.db import models

# Create your models here.
class Stocks(models.Model):
    market = models.CharField(max_length = 200)
    stock_name = models.CharField(max_length = 200)
    gained_values = models.CharField(max_length = 200)
    date_created = models.DateTimeField(auto_now=True)
