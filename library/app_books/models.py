from django.db import models
from django.db.models import CASCADE


class Genres(models.Model):
    title = models.CharField(max_length=50, verbose_name="жанр")

    class Meta:
        verbose_name = "genre"

    def __str__(self):
        return self.title


class Authors(models.Model):
    last_name = models.CharField(max_length=50, verbose_name="фамилия")
    first_name = models.CharField(max_length=50, verbose_name="имя")
    date_of_birth = models.DateField(null=True, verbose_name="дата рождения")

    class Meta:
        verbose_name = "author"

    def __str__(self):
        return f"{self.last_name} {self.first_name}"


class Shelves(models.Model):
    title = models.CharField(max_length=25, verbose_name="полка")

    class Meta:
        verbose_name = "shelve"

    def __str__(self):
        return self.title


class Books(models.Model):
    title = models.CharField(max_length=100, verbose_name="название")
    publication = models.DateField(null=True, verbose_name="дата издания")
    genre = models.ForeignKey(Genres, on_delete=CASCADE, null=True, verbose_name="жанр")
    author = models.ForeignKey(
        Authors, on_delete=CASCADE, null=True, verbose_name="автор"
    )
    shelves = models.ForeignKey(
        Shelves, on_delete=CASCADE, null=True, verbose_name="полка"
    )

    class Meta:
        verbose_name = "book"

    def __str__(self):
        return self.title
