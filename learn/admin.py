from django.contrib import admin
from  .models import learn

# Register your models here.
class learnAdmin(admin.ModelAdmin):
    list_display = ('category', 'title','date')
    list_display_links = ('date',)
    list_editable = ('category','title')
    list_filter = ('date', 'category',)
    search_fields = ['category', 'title', 'date']
   


admin.site.register(learn, learnAdmin)