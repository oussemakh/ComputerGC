from django.db import models

# Create your models here.
class PROD(models.Model):
    product_name = models.CharField(max_length=250,null=True)
    product_discription = models.CharField(max_length=250)
    product_detail = models.TextField(default='put your idea')
    product_price = models.FloatField()
    product_img = models.ImageField(blank=True, default='default.png')
    product_quantite = models.IntegerField()
    date = models.DateField(auto_now=True)
    slug= models.SlugField(default='name-slug')



    def __str__(self):
        return self.product_name