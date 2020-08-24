"""Business model"""

# Django
from django.db import models
from django.core.validators import RegexValidator

# Utilities
from api.utils.models import BaseModel

class Business(BaseModel):
    """ Business model. """

    name = models.CharField(max_length = 150)
    image = models.CharField(max_length=150)
    phone_regex = RegexValidator(
        regex=r'\+?1?\d{9,15}$',
        message='Phone nubmer must be entered in the format : +999999999. Up to 15 digits allowed.'
    )
    phone_number = models.CharField(
        validators=[phone_regex], 
        max_length=17, 
        blank=True
    )
    email = models.EmailField(
        'email address',
        unique=True,
        error_messages={
            'unique': 'A user with that email already exists.'
        }
    )
    rating = models.IntegerField()
    description = models.CharField(max_length=250)

    # admin_profiles = models.ManyToManyField('guatudu.AdminProfile')
    
    def __str__(self):
        """ Return business string representation"""
        return str(self.name)
    
    class Meta:
        db_table = 'business'

