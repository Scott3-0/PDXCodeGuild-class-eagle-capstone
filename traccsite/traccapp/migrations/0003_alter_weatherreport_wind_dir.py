# Generated by Django 3.2.3 on 2021-07-08 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('traccapp', '0002_alter_weatherreport_wind_vel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weatherreport',
            name='wind_dir',
            field=models.CharField(choices=[('0', 'No wind'), ('000', 'North'), ('045', 'Northeast'), ('090', 'East'), ('135', 'Southeast'), ('180', 'South'), ('225', 'Southwest'), ('270', 'West'), ('315', 'Northwest')], max_length=3),
        ),
    ]
