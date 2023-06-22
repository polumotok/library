from django.db import models
from app_books.models import Book, Shelve


class Reader(models.Model):
    """
    Модель читатель

    last_name - фамилия читателя
    first_name - имя читателя
    """
    last_name = models.CharField(max_length=50, null=True)
    first_name = models.CharField(max_length=50, null=True)

    def __str__(self):
        """
        Функция возвращает фамилию и имя читателя
        """
        return f"{self.last_name} {self.first_name}"


class ReaderBook(models.Model):
    """
    Модель читатель книги

    reader - инфармация о читателе
    book - информация о книге
    date_of_taking - дата когда читатель взял книгу
    date_of_return - дата когда читатель вернул книгу
    days_of_use - на сколько дней выдается книга
    """
    reader = models.ForeignKey(Reader, on_delete=models.CASCADE, null=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, null=False, related_name="reader")
    date_of_taking = models.DateField(auto_now_add=True)
    date_of_return = models.DateField(null=True, blank=True)
    days_of_use = models.IntegerField()
    @property
    def get_return_time(self):
        """
        Функция возвращает разницу дней с момента взятия книги читателем до момента ее возврата
        """
        if self.date_of_return is not None:
            timing = (self.date_of_return - self.date_of_taking).days
            if timing <= self.days_of_use:
                return (timing)
            else:
                return (timing, "Проссрочена")

class LocationBook(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="location")
    shelve = models.ForeignKey(Shelve, on_delete=models.CASCADE, null=True, blank=True)
    reader = models.ForeignKey(Reader, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        if self.shelve is not None:
            return f"Полка - {self.shelve}"
        else:
            return f"Читатель - {self.reader}"