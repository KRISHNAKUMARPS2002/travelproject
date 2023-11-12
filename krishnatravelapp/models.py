from django.db import models

# Create your models here.
class place(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pictures')
    desc = models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField(default=False)

class vlog(models.Model):
    month = models.CharField(max_length=100)
    heading = models.CharField(max_length=1000)
    desc = models.CharField(max_length=1000)
    img = models.ImageField(upload_to='pictures')