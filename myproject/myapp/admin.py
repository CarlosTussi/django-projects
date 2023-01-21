from django.contrib import admin
from .models import MenuCategory, Menu, Book, Logger

# Register your models here.
admin.site.register(Menu)
admin.site.register(MenuCategory)
admin.site.register(Book)
admin.site.register(Logger)