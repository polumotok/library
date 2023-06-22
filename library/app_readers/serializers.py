from rest_framework import serializers

from .models import Reader, ReaderBook, LocationBook
from app_books.serializers import BookSerializer


class ReadersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reader
        fields = ["first_name", "last_name"]


class ReadersBooksSerializer(serializers.ModelSerializer):
    reader = ReadersSerializer()
    books = BookSerializer()

    class Meta:
        model = ReaderBook
        fields = ["reader", "date_of_taking", "date_of_return", "get_return_time", "books"]

class LocationBookSerializer(serializers.ModelSerializer):
    book = BookSerializer()
    class Meta:
        model = LocationBook
        fields = ["book"]
