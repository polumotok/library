from django.contrib import admin
from app_books.models import Books, Genres, Authors, Shelves


class GenresAdmin(admin.ModelAdmin):
    list_display = ("id", "title")


class AuthorsAdmin(admin.ModelAdmin):
    list_display = ("id", "last_name", "first_name")


class ShelvesAdmin(admin.ModelAdmin):
    list_display = ("id", "title")


class BooksAdmin(admin.ModelAdmin):
    list_display = ("id", "title")


admin.site.register(Genres, GenresAdmin)
admin.site.register(Authors, AuthorsAdmin)
admin.site.register(Shelves, ShelvesAdmin)
admin.site.register(Books, BooksAdmin)
