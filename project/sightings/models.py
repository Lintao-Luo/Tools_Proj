from django.db import models

# Create your models here

class SquirrelData(models.Model):
    x = models.FloatField(db_column='X', blank=True, null=True)  # Field name made lowercase.
    y = models.FloatField(db_column='Y', blank=True, null=True)  # Field name made lowercase.
    unique_squirrel_id = models.TextField(db_column='Unique Squirrel ID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    hectare = models.TextField(db_column='Hectare', blank=True, null=True)  # Field name made lowercase.
    shift = models.TextField(db_column='Shift', blank=True, null=True)  # Field name made lowercase.
    date = models.IntegerField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    hectare_squirrel_number = models.IntegerField(db_column='Hectare Squirrel Number', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    age = models.TextField(db_column='Age', blank=True, null=True)  # Field name made lowercase.
    primary_fur_color = models.TextField(db_column='Primary Fur Color', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    highlight_fur_color = models.TextField(db_column='Highlight Fur Color', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    combination_of_primary_and_highlight_color = models.TextField(db_column='Combination of Primary and Highlight Color', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    color_notes = models.TextField(db_column='Color notes', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    location = models.TextField(db_column='Location', blank=True, null=True)  # Field name made lowercase.
    above_ground_sighter_measurement = models.TextField(db_column='Above Ground Sighter Measurement', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    specific_location = models.TextField(db_column='Specific Location', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    running = models.IntegerField(db_column='Running', blank=True, null=True)  # Field name made lowercase.
    chasing = models.IntegerField(db_column='Chasing', blank=True, null=True)  # Field name made lowercase.
    climbing = models.IntegerField(db_column='Climbing', blank=True, null=True)  # Field name made lowercase.
    eating = models.IntegerField(db_column='Eating', blank=True, null=True)  # Field name made lowercase.
foraging = models.IntegerField(db_column='Foraging', blank=True, null=True)  # Field name made lowercase.
    other_activities = models.TextField(db_column='Other Activities', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    kuks = models.IntegerField(db_column='Kuks', blank=True, null=True)  # Field name made lowercase.
    quaas = models.IntegerField(db_column='Quaas', blank=True, null=True)  # Field name made lowercase.
    moans = models.IntegerField(db_column='Moans', blank=True, null=True)  # Field name made lowercase.
    tail_flags = models.IntegerField(db_column='Tail flags', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    tail_twitches = models.IntegerField(db_column='Tail twitches', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    approaches = models.IntegerField(db_column='Approaches', blank=True, null=True)  # Field name made lowercase.
    indifferent = models.IntegerField(db_column='Indifferent', blank=True, null=True)  # Field name made lowercase.
    runs_from = models.IntegerField(db_column='Runs from', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    other_interactions = models.TextField(db_column='Other Interactions', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    lat_long = models.TextField(db_column='Lat/Long', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    zip_codes = models.FloatField(db_column='Zip Codes', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    community_districts = models.IntegerField(db_column='Community Districts', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    borough_boundaries = models.IntegerField(db_column='Borough Boundaries', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    city_council_districts = models.IntegerField(db_column='City Council Districts', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    police_precincts = models.IntegerField(db_column='Police Precincts', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'Squirrel_Data'
