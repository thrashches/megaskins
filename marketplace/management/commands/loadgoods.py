import json
from django.conf import settings
from django.core.management import BaseCommand
from marketplace.models import Product


class Command(BaseCommand):
    help = 'Загрузка товаров в базу.'

    def handle(self, *args, **options):
        with open(settings.BASE_DIR / 'goods.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
        Product.objects.bulk_create([Product(**item) for item in data])
        print('Товары успешно добавлены в базу!')
