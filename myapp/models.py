from django.db import models

# Create your models here.

class HeroArea(models.Model):
    icon_img = models.ImageField(upload_to='hero_area', blank=True, null=True)  
    icon_title = models.CharField(max_length=20 , blank=True, null=True)
    bg_img = models.ImageField(upload_to='hero_area', blank=True, null=True)
    title = models.CharField(max_length=20 , blank=True, null=True)
    note = models.CharField(max_length=100 , blank=True, null=True)
    video = models.URLField(null=True,blank=True)