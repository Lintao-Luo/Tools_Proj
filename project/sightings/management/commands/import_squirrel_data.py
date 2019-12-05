from django.core.management.base import BaseCommand
import pandas as pd
import sys
import csv, sqlite3

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('file_url', nargs='+', type=str, help='URL of the data file')

    def handle(self, *args, **options):
        #print(options['file_url'])
        conn= sqlite3.connect("db.sqlite3")
        df = pd.read_csv(options['file_url'][0])
        df.to_sql(options['file_url'][0].replace('.csv',''), conn, if_exists='append', index=False)
        
        #df = pd.DataFrame([(0,1),(2,3)],columns=['col1','col2'])
        print('\nSuccess!\n')    

    
