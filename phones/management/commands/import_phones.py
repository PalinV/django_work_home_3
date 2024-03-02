import csv

from django.core.management.base import BaseCommand
from django.template.defaultfilters import slugify
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for phone in phones:
            #release_date = phone['release_date'][-4:] + '-' + phone['release_date'][3:5] + '-' + phone['release_date'][0:2]
            Phone.objects.create(
                id=int(phone['id']), name=phone['name'],
                price=int(phone['price']), image=phone['image'],
                release_date=phone['release_date'],
                lte_exists=phone['lte_exists'],
                slug=slugify(phone['name']),
            )

