from rest_framework import serializers
from .models import News, OilPrice, StockMarket, Prediction

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'

class OilSerializer(serializers.ModelSerializer):
    class Meta:
        model = OilPrice
        fields = '__all__'

class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockMarket
        fields = '__all__'

class PredictionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prediction
        fields = '__all__'