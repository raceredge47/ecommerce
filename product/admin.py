from django.contrib import admin
from .models import Product    # Importing product model from models.py
# Register your models here.


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """
     Register model in admin panel with some modification

    """
    list_display = ('id', 'Name', 'Description', 'Image', 'Price', 'Stock', 'created_on', 'updated_on')  # Display all these fields in admin panel product tab.
    list_filter = ('created_on', 'updated_on')                                                           # Filter with date.
    list_per_page = 50                                                                                   # View 50 records per page.
    search_fields = ('Name__startswith',)                                                                # Adding search field in admin panel.
