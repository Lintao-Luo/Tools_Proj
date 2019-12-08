# Generated by Django 2.2.7 on 2019-12-06 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Squirrel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.FloatField(help_text='Latitude')),
                ('longitude', models.FloatField(help_text='Longitude')),
                ('squirrel_id', models.CharField(help_text='Unique Squirrel ID', max_length=256)),
                ('shift', models.CharField(choices=[('AM', 'AM'), ('PM', 'PM')], help_text='Shift', max_length=20)),
                ('date', models.DateField(help_text='Date')),
                ('age', models.CharField(blank=True, choices=[('Adult', 'Adult'), ('Juvenile', 'Juvenile')], help_text='Age', max_length=100, null=True)),
                ('color', models.CharField(blank=True, choices=[('Gray', 'Gray'), ('Cinnamon', 'Cinnamon'), ('Black', 'Black')], help_text='Primary Fur Color', max_length=100, null=True)),
                ('location', models.CharField(blank=True, choices=[('Ground Plane', 'Ground Plane'), ('Above Ground', 'Above Ground')], help_text='Location', max_length=100, null=True)),
                ('specific_location', models.CharField(blank=True, help_text='Specific Location', max_length=256, null=True)),
                ('running', models.BooleanField(help_text='Running')),
                ('chasing', models.BooleanField(help_text='Chasing')),
                ('climbing', models.BooleanField(help_text='Climbing')),
                ('eating', models.BooleanField(help_text='Eating')),
                ('foraging', models.BooleanField(help_text='Foraging')),
                ('other_activities', models.CharField(blank=True, help_text='Other Activities', max_length=256, null=True)),
                ('kuks', models.BooleanField(help_text='Kuks')),
                ('quaas', models.BooleanField(help_text='Quaas')),
                ('moans', models.BooleanField(help_text='Moans')),
                ('tail_flag', models.BooleanField(help_text='Tail flags')),
                ('tail_twitches', models.BooleanField(help_text='Tail twitches')),
                ('approaches', models.BooleanField(help_text='Approaches')),
                ('indifferent', models.BooleanField(help_text='Indifferent')),
                ('runs_from', models.BooleanField(help_text='Runs from')),
            ],
        ),
    ]
