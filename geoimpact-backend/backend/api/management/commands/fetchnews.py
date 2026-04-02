from django.core.management.base import BaseCommand
from api.news_fetcher import fetch_news

class Command(BaseCommand):
    help = 'Fetch news and store in database'

    def handle(self, *args, **kwargs):
        fetch_news()
        self.stdout.write(self.style.SUCCESS('News fetched successfully'))