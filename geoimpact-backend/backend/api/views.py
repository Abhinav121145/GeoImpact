from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import News, OilPrice, StockMarket, Prediction
from .serializers import NewsSerializer, OilSerializer, StockSerializer, PredictionSerializer

import sys
import os

# Add ML model path
sys.path.append(os.path.join(os.path.dirname(__file__), '../../ml_model'))

from predict import predict_market


# ---------------- NEWS API ----------------
@api_view(['GET'])
def news(request):
    news_data = News.objects.all().order_by('-date')
    serializer = NewsSerializer(news_data, many=True)
    return Response(serializer.data)


# ---------------- OIL API ----------------
@api_view(['GET'])
def oil(request):
    oil_data = OilPrice.objects.all().order_by('-date')
    serializer = OilSerializer(oil_data, many=True)
    return Response(serializer.data)


# ---------------- STOCK API ----------------
@api_view(['GET'])
def stocks(request):
    stock_data = StockMarket.objects.all().order_by('-date')
    serializer = StockSerializer(stock_data, many=True)
    return Response(serializer.data)


# ---------------- PREDICTION API (ML) ----------------
@api_view(['GET'])
def prediction(request):
    try:
        news = News.objects.last()
        oil = OilPrice.objects.last()
        stock = StockMarket.objects.last()

        oil_pred, stock_pred = predict_market(
            news.sentiment,
            news.impact_score,
            oil.price,
            stock.price
        )

        return Response({
            "oil_prediction": round(oil_pred, 2),
            "stock_prediction": round(stock_pred, 2)
        })

    except Exception as e:
        return Response({
            "error": str(e)
        })