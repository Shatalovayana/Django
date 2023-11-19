import json

from django.core.management import BaseCommand

from catalog.models import Category, Product


class Command(BaseCommand):
    def handle(self, *args, **options):
        Category.objects.all().delete()
        Product.objects.all().delete()
        with open('catalog_data.json', 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
        for info in data:
            if info['model'] == 'catalog.category':
                Category.objects.create(pk=info['pk'], **info['fields'])
            elif info['model'] == 'catalog.product':
                product = info['fields']
                category_id = product.pop('category')
                Product.objects.create(pk=info['pk'], category_id=category_id, **product)

