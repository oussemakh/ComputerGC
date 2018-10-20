from django.contrib import admin
from .models import PROD
# Register your models here.



class PRODAdmin(admin.ModelAdmin):
    list_display = ('product_name','product_price','product_quantite','date')
    list_editable = ("product_price","product_quantite")
    list_filter = ('product_quantite','date',)
    search_fields = ['product_price','product_quantite','date','product_name']

admin.site.register(PROD, PRODAdmin)