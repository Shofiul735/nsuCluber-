from django.db import models

# Create your models here.
class AllAdmins(models.Model):
    club_name = models.CharField(max_length = 20,primary_key = True)
    password = models.CharField(max_length = 30 )