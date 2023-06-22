from django.contrib import admin
from app_books.models import Book, Genre, Author, Shelve


class GenresAdmin(admin.ModelAdmin):
    list_display = ("id", "title")


class AuthorsAdmin(admin.ModelAdmin):
    list_display = ("id", "last_name", "first_name")


class ShelvesAdmin(admin.ModelAdmin):
    list_display = ("id", "title")


class BooksAdmin(admin.ModelAdmin):
    list_display = ("id", "title")




admin.site.register(Genre, GenresAdmin)
admin.site.register(Author, AuthorsAdmin)
admin.site.register(Shelve, ShelvesAdmin)
admin.site.register(Book, BooksAdmin)
