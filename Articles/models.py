from django.db import models

class Article(models.Model):
    Title = models.CharField(max_length=250)
    Disc = models.CharField(max_length=400)
    Body = models.TextField()
    pic = models.ImageField(blank=True, default='default.png')
    pic2 = models.ImageField(blank=True, default='default1.png')
    slug1 = models.SlugField()
    Date = models.DateField(auto_now=True, blank=True,null=True)



    def __str__(self):
        return self.Title