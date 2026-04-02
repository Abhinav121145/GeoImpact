from django.core.management.base import BaseCommand
from api.market_fetcher import fetch_market_data
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
import json

class Command(BaseCommand):
    help = 'Fetch market data'

    def handle(self, *args, **kwargs):
        data = fetch_market_data()

        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "live_group",
            {
                "type": "send_live_data",
                "data": data
            }
        )

        self.stdout.write(self.style.SUCCESS('Market data fetched and sent live'))