from rest_framework import serializers
from .models import Book, Author, Genre


class AuthorSerializer(serializers.ModelSerializer):
    """
    Сериалайзер модели автор
    """
    class Meta:
        model = Author
        fields = [
            "first_name",
            "last_name",
        ]

class GenreSerializer(serializers.ModelSerializer):
    """
    Сериалайзер модели жанр
    """
    class Meta:
        model = Genre
        fields = ["title"]
class BookSerializer(serializers.ModelSerializer):
    """
    Сериалайзер модели книга

    location - вложенный сериалайзер место нахождения книги
    authors - вложенный сериалайзер списка авторов
    genres - вложенный сериалайзер списка жанров
    """
    location = serializers.StringRelatedField(many=True)
    authors = AuthorSerializer(many=True)
    genres = GenreSerializer(many=True)
    class Meta:
        model = Book
        fields = [
            "id",
            "title",
            "publication",
            "authors",
            "genres",
            "location",
        ]


