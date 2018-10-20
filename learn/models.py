from django.db import models

# Create your models here.



class learn(models.Model):
    category = models.CharField(max_length=250)
    title = models.CharField(max_length=250)
    disc = models.CharField(max_length=250)
    body = models.TextField()
    img = models.ImageField(default='defualt.png', blank=True)
    file = models.FileField()
    slug2 = models.SlugField(blank=True, null=True)
    date = models.DateField(auto_now=True)
