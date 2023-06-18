from django.contrib import admin

from .models import Readers, ReadersBooks


@admin.register(ReadersBooks)
class ReadersBooks(admin.ModelAdmin):
    list_display = ["reader", "books"]
    fields = ["reader", "books"]


admin.site.register(Readers)
