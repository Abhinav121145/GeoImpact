# GeoImpact – AI Geopolitical Intelligence Dashboard

GeoImpact is an AI-powered full-stack web application that analyzes geopolitical news and predicts its impact on oil prices and stock markets in real time.

## Features

- Live geopolitical news sentiment analysis
- Oil price tracking (Yahoo Finance API)
- Stock market tracking (S&P 500, NASDAQ, NIFTY)
- Machine learning model for market prediction
- Real-time dashboard with WebSocket updates
- Dark-themed professional analytics UI
- Django REST API backend
- React frontend dashboard

## Tech Stack

Frontend:
- React.js
- Recharts
- WebSockets

Backend:
- Django
- Django REST Framework
- Django Channels

Machine Learning:
- Scikit-learn
- Pandas
- NLP (TextBlob)

APIs:
- NewsAPI
- Yahoo Finance API

## System Architecture

News API → Sentiment Analysis → Impact Score  
Market Data API → Oil & Stock Prices  
ML Model → Market Prediction  
Django API → React Dashboard  
WebSocket → Live Updates  

## How to Run

### Backend
```bash
cd backend
pip install -r requirements.txt
python manage.py runserver

