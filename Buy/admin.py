from django.contrib import admin
from django import forms  
from .models import by


# Register your models here.



class byAdmin(admin.ModelAdmin):
   
   
   list_display = ('address','phone','email','cin','first_name','last_name','date','product_name')
   list_filter = ('date','address',)
   search_fields = ['address','phone','email','cin','first_name','last_name','date']
admin.site.register(by, byAdmin)



