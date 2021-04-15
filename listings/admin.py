from django.contrib import admin
from .models import Listing

# Register your models here.


class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'price',
                    'list_date', 'realtor')  # Show data
    list_display_links = ('id', 'title')  # Visible click option
    list_filter = ('realtor',)  # ',' must for identifying tuple or list
    list_editable = ('is_published',)
    search_fields = ('title', 'description', 'address',
                     'city', 'state', 'zipcode', 'price')
    list_per_page = 25


admin.site.register(Listing, ListingAdmin)  # Register model
