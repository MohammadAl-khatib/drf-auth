from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Book


# admin.site.register(Book)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'genre', 'available']