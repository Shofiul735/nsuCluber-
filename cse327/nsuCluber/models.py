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

class EventPost(models.Model):
    title = models.CharField(max_length = 30)
    start = models.Chaend = models.CharField(max_length = 20)
    end = models.CharField(max_length = 20)
    place = models.CharField(max_length = 20)
    owner = models.ForeignKey(AllAdmins,on_delete = models.CASCADE)
    eventSummary = models.CharField(max_length = 100)
    eventDetails = models.TextField()
    keyWord = models.CharField(max_length = 50)
    
    def __str__(self):
        return self.title
    