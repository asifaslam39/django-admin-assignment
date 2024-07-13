# mainApp/management/commands/load_csv.py

import csv
from django.core.management.base import BaseCommand
from mainApp.models import Dish
import os
from django.conf import settings

class Command(BaseCommand):
    help = 'Load data from CSV file into the database'

    def handle(self, *args, **kwargs):
        file_path = os.path.join(settings.BASE_DIR, 'mainApp/dataset/restaurants_small.csv')
        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                try:
                    lat, lon = map(float, row['lat_long'].split(','))
                    Dish.objects.create(
                        name=row['name'],
                        items=row['items'],
                        location=row['location'],
                        latitude=lat,
                        longitude=lon,

                        full_details=row['full_details']
                    )
                except Exception as e:
                    self.stdout.write(self.style.ERROR(f"Error: {e}"))

        self.stdout.write(self.style.SUCCESS('Successfully loaded data into the database'))
