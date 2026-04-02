from django.contrib import admin
from .models import News, OilPrice, StockMarket, Prediction

admin.site.register(News)
admin.site.register(OilPrice)
admin.site.register(StockMarket)
admin.site.register(Prediction)