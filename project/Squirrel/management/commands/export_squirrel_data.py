from django.core.management.base import BaseCommand
from Squirrel.models import Squirrel
from django.utils import timezone
import pandas as pd
import numpy as np
import datetime

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('csv_file')

    def handle(self, *args, **options):
        # df = pd.read_csv(options['csv_file'])
        cols = ['X', 'Y', 'Unique Squirrel ID', 'Shift', 'Date', 'Age', 'Primary Fur Color', 'Location', 'Specific Location', 'Running', 'Chasing', 'Climbing', 'Eating', 'Foraging', 'Other Activities', 'Kuks', 'Quaas', 'Moans', 'Tail flags', 'Tail twitches', 'Approaches', 'Indifferent', 'Runs from']
        item_ = list()
        total_items = list()
        for item in Squirrel.objects.values():
            item_ = list(item.values())[1:]
            item_[0], item_[1] = item_[1], item_[0]
            item_[4] = item_[4].strftime('%m%d%Y')
            total_items.append(item_)

        df = pd.DataFrame(total_items, columns=cols)
        df.to_csv(options['csv_file'], index=False)
        print('Export Success!')

