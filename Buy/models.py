from django.db import models
from product.models import PROD

# Create your models here.
defl = 1
class by(models.Model):
    
    
    
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.IntegerField()
    cin = models.IntegerField()
    address = models.CharField(max_length=250, default=' city  street house_number')
    date = models.DateTimeField(auto_now=True)
    product_name =  models.ForeignKey(PROD, on_delete=models.CASCADE,default=defl)


    def __str__(self):
        return self.first_name