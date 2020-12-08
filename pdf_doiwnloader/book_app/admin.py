from django.contrib import admin

from .models import Category, Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['book_name','book_author','category','published_year','book_isbn']
    list_filter = ['book_name','book_author','category','book_isbn']
    prepopulated_fields = {'slug':('book_name',)}

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

