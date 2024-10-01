from django.contrib import admin
from .models import Rating
from .models import Laptop

class RatingAdmin(admin.ModelAdmin):
    list_display = ('review', 'rating', 'recommended', 'laptop') 
    search_fields = ('review',)  
    list_filter = ('rating', 'recommended')  

admin.site.register(Rating, RatingAdmin)

class LaptopAdmin(admin.ModelAdmin):
    list_display = ('laptop_name', 'spec', 'price', 'total_rating')  
    search_fields = ('laptop_name', 'spec')  
    list_filter = ('price',)  
    exclude = ('total_rating',)

admin.site.register(Laptop, LaptopAdmin)

