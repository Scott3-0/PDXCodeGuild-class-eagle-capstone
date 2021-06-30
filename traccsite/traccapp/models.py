from django.db import models

# Create your models here.
class User(models.Model):
    user_id = models.IntegerField()
    username = models.CharField(max_length=25)
    password = models.CharField(max_length=50)

class SavedLoc(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lat = models.IntegerField()
    lon = models.IntegerField()