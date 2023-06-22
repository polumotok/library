from django.contrib import admin

from .models import Reader, ReaderBook, LocationBook


@admin.register(ReaderBook)
class ReadersBooks(admin.ModelAdmin):
    list_display = ["reader", "book"]
    fields = ["reader", "book"]

class LocationBookAdmin(admin.ModelAdmin):
    list_display = ("id", "shelve", "reader")

admin.site.register(Reader)
admin.site.register(LocationBook, LocationBookAdmin)