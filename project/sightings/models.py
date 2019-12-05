from django.db import models

class Sightings(models.Model):
    Latitude = models.FloatField(db_column='X', blank=True, null=True)
    Longitude = models.FloatField(db_column='Y', blank=True, null=True)
    Unique_Squirrel_ID = models.CharField(db_column='Unique Squirrel ID', max_length=200, blank=True, null=True)
    Shift = models.TextField(db_column='Shift', blank=True, null=True)
    date = models.IntegerField(db_column='Date', blank=True, null=True)  
    age = models.TextField(db_column='Age', blank=True, null=True)
    primary_fur_color = models.TextField(db_column='Primary Fur Color', blank=True, null=True)
    location = models.TextField(db_column='Location', blank=True, null=True)      
    specific_location = models.TextField(db_column='Specific Location', blank=True, null=True)
    running = models.IntegerField(db_column='Running', blank=True, null=True)
    chasing = models.IntegerField(db_column='Chasing', blank=True, null=True)
    climbing = models.IntegerField(db_column='Climbing', blank=True, null=True) 
    eating = models.IntegerField(db_column='Eating', blank=True, null=True) 
    foraging = models.IntegerField(db_column='Foraging', blank=True, null=True)
    other_activities = models.TextField(db_column='Other Activities', blank=True, null=True)
    kuks = models.IntegerField(db_column='Kuks', blank=True, null=True)
    quaas = models.IntegerField(db_column='Quaas', blank=True, null=True)
    moans = models.IntegerField(db_column='Moans', blank=True, null=True)
    tail_flags = models.IntegerField(db_column='Tail flags', blank=True, null=True)
    tail_twitches = models.IntegerField(db_column='Tail twitches', blank=True, null=True)
    approaches = models.IntegerField(db_column='Approaches', blank=True, null=True)
    indifferent = models.IntegerField(db_column='Indifferent', blank=True, null=True)
    runs_from = models.IntegerField(db_column='Runs from', blank=True, null=True)

    def __str__(self):
        return self.Unique_Squirrel_ID

   



