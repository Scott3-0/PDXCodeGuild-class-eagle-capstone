from django.db import models

# Create your models here.
class WeatherReport(models.Model):
    sky_condition_choices = [
        ('SKC', 'Clear skies'),
        ('FEW', 'Few clouds'),
        ('SCT', 'Scattered clouds'),
        ('BKN', 'Broken skies'),
        ('OVC', 'Overcast')
    ]
    wind_dir_choices = [
        ('NAN', 'No wind'),
        ('000', 'North'),
        ('045', 'Northeast'),
        ('090', 'East'),
        ('135', 'Southeast'),
        ('180', 'South'),
        ('225', 'Southwest'),
        ('270', 'West'),
        ('315', 'Northwest')
    ]

    location = models.CharField(max_length=50)
    date = models.DateField()
    time = models.TimeField()
    sky_condition = models.CharField(max_length=3, choices=sky_condition_choices)
    wind_dir = models.CharField(max_length=3, choices=wind_dir_choices)
    wind_vel = models.FloatField(default=0)
    temp = models.FloatField()
