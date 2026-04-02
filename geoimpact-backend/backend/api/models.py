from django.db import models

class News(models.Model):
    title = models.CharField(max_length=500)
    sentiment = models.FloatField()
    impact_score = models.FloatField()
    date = models.DateField()

class OilPrice(models.Model):
    price = models.FloatField()
    date = models.DateField()

class StockMarket(models.Model):
    index_name = models.CharField(max_length=100)
    price = models.FloatField()
    date = models.DateField()

class Prediction(models.Model):
    oil_prediction = models.FloatField()
    stock_prediction = models.FloatField()
    date = models.DateField()