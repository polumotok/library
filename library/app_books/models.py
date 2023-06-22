from django.db import models



class Genre(models.Model):
    """Модель жанр.

    title - название жанра
    """
    title = models.CharField(max_length=50, verbose_name="Название")

    class Meta:
        verbose_name = "genre"

    def __str__(self):
        """
        Функция возвращает название жанра
        """
        return self.title


class Author(models.Model):
    """Модель автор
    last_name - Фамилия автора
    first_name - Имя автора
    date_of_birth - дата рождения автора
    """
    last_name = models.CharField(max_length=50, verbose_name="Фамилия")
    first_name = models.CharField(max_length=50, verbose_name="Имя")
    date_of_birth = models.DateField(verbose_name="Дата рождения")

    class Meta:
        verbose_name = "author"

    def __str__(self):
        """
        Функция возвращает фамилию и имя автора
        """
        return f"{self.last_name} {self.first_name}"


class Shelve(models.Model):
    """Модель Полка

    title - название полки
    """
    title = models.CharField(max_length=25, verbose_name="Название")

    class Meta:
        verbose_name = "shelve"

    def __str__(self):
        """
        Функция возвращает название полки
        """
        return self.title


class Book(models.Model):
    """Модель книга.

    title - название книги
    publication - дата издания книги
    genres - жанры книги
    authors - авторы книги
    location - место нахождение книги
    """
    title = models.CharField(max_length=100, verbose_name="Название")
    publication = models.DateField(null=True, verbose_name="Дата издания")
    genres = models.ManyToManyField(Genre, verbose_name="Жанры")
    authors = models.ManyToManyField(Author, verbose_name="Авторы")

    class Meta:
        verbose_name = "book"


    def __str__(self):
        """
        Функция возвращает название книги
        """
        return self.title
