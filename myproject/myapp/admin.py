from django.contrib import admin
from .models import MenuCategory, Menu, Book

# Register your models here.
admin.site.register(Menu)
admin.site.register(MenuCategory)
admin.site.register(Book)