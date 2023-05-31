from django.db import models
from app_books.models import Books


class Readers(models.Model):
    last_name = models.CharField(max_length=50, null=True)
    first_name = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.last_name


class ReadersBooks(models.Model):
    reader = models.ForeignKey(
        Readers, on_delete=models.CASCADE, null=True, related_name="reader"
    )
    books = models.ForeignKey(Books, on_delete=models.CASCADE, null=False)
    date_of_taking = models.DateField(auto_now_add=True)
    date_of_return = models.DateField(null=True, blank=True)
    delay = models.BooleanField(default=False)

    def diff_date(self):
        return (self.date_of_return - self.date_of_taking).days
