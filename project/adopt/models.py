from django.db import models

from django.utils.translation import gettext as _

class Pet(models.Model):
    birth_date = models.DateField(
            help_text=_('Birth date'),
    )

    MALE = 'male'
    FEMALE = 'female'
    OTHER = 'other'

    SEX_CHOICES = (
            (MALE, 'MALE'),
            (FEMALE, 'FEMALE'),
            (OTHER, 'OTHERS'),
    )

    species = models.CharField(
            help_text = _('species of animal'),
            max_length = 100,
    )

    name = models.CharField(
            help_text = _('name of animal'),
            max_length = 100,
    )



    sex = models.CharField(
            help_text = _('sex of pet'),
            max_length = 16,
            choices = SEX_CHOICES,
            default = OTHER,
    )

    def __str__(self):
        return self.name

# Create your models here.
