from django.db import models

# Create your models here.

class MyData(models.Model):
    name = models.CharField(max_length=100)
    value = models.IntegerField()

    def __str__(self):
        return self.name
    
class Signals(models.Model):
    stock_name = models.CharField(max_length=100)
    strategy_name = models.CharField(max_length=100)
    signal = models.CharField(max_length=100)
    date_time = models.DateField()
    price = models.FloatField()
    final_portfolio_value = models.FloatField()

    def __str__(self):
        return f"{self.stock_name} - {self.strategy_name} - {self.signal} - {self.date} - {self.time} - {self.price} - {self.final_portfolio_value}"
