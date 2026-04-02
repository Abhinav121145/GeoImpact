import requests
import os
from textblob import TextBlob
from datetime import datetime
from .models import News

API_KEY = os.getenv("NEWS_API_KEY")

def get_sentiment(text):
    analysis = TextBlob(text)
    return analysis.sentiment.polarity

def get_impact_score(sentiment, title):
    title = title.lower()

    if "war" in title or "attack" in title or "missile" in title:
        return -0.9
    elif "sanction" in title or "conflict" in title:
        return -0.6
    elif "peace" in title or "agreement" in title:
        return 0.7
    elif "growth" in title or "economy" in title:
        return 0.5
    else:
        return sentiment



def fetch_news():
    url = f"https://newsapi.org/v2/everything?q=war OR oil OR economy OR stock market&language=en&sortBy=publishedAt&apiKey={API_KEY}"
    response = requests.get(url)
    data = response.json()

    if "articles" not in data:
        print("Error:", data)
        return

    articles = data["articles"]

    for article in articles:
        title = article["title"]

        if not title:
            continue

        sentiment = get_sentiment(title)
        impact = get_impact_score(sentiment, title)

        News.objects.create(
            title=title,
            sentiment=sentiment,
            impact_score=impact,
            date=datetime.today()
        )

    print("News stored successfully")