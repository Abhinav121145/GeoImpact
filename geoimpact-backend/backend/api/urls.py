from django.urls import path
from . import views

urlpatterns = [
    path('news/', views.news),
    path('oil/', views.oil),
    path('stocks/', views.stocks),
    path('prediction/', views.prediction),
]