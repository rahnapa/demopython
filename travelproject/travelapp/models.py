from django.db import models
# Create your models here.
class place(models.Model):
    name=models.CharField(max_length=250)
    image=models.ImageField(upload_to='pics')
    description=models.TextField()
class people(models.Model):
    name1=models.CharField(max_length=250)
    image1=models.ImageField(upload_to='pics')
    description1=models.TextField()