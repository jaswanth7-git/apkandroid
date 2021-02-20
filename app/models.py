from django.db import models

# Create your models here.
class Apk(models.Model):
    imgurl = models.CharField(max_length=10000)
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=50,default='game' )
    dlink = models.CharField(max_length=200)
    def __str__(self):
        return self.name