from django import forms    
from .models import by
from product.models import PROD



class BuyForm(forms.ModelForm):
    #product_name =forms.ModelChoiceField(queryset=PROD.objects.all())

    class Meta:
        model = by
        fields = ('first_name','last_name', 'email', 'phone', 'cin','address','product_name',)
    
   