from django.db import models

# Create your models here.
class AllAdmins(models.Model):
    club_name = models.CharField(max_length = 20,primary_key = True)
    password = models.CharField(max_length = 30 )
    def __str__(self):
        return self.club_name
    
class ExistingMember(models.Model):
    nsu_id = models.IntegerField()
    name = models.CharField(max_length = 30)
    club_name = models.ForeignKey(AllAdmins,on_delete=models.CASCADE)
    position = models.CharField(max_length = 10)
    def __str__(self):
        return self.name