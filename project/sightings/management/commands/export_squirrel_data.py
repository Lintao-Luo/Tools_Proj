from django.core.management.base import BaseCommand
import pandas as pd
import csv, sqlite3

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('file_url', nargs='+', type=str, help='URL of the data file')

    def handle(self, *args, **options):
        conn = sqlite3.connect("db.sqlite3")
        cursor = conn.cursor()

        sql_columns = 'PRAGMA table_info("Squirrel_Data")'
        sql = 'SELECT * from Squirrel_Data'

        cursor.execute(sql_columns)
        col_value = cursor.fetchall()
        
        cursor.execute(sql)
        data = cursor.fetchall()

        columns_ = list()
        
        for i in range(36):
            columns_.append(col_value[i][1])

        df = pd.DataFrame(data, columns=columns_)
        df.to_csv(options['file_url'][0], index=False)

        print('\nSuccess!\n')
