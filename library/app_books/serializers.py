from rest_framework import serializers

from .models import *

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genres
        fields = ['title']

class BookSerializer(serializers.ModelSerializer):
    # genre = serializers.StringRelatedField()
    # author = serializers.StringRelatedField()
    # shelves = serializers.StringRelatedField()

    class Meta:
        model = Books
        fields = [
            "id",
            "title",
            "publication",
            "author",
            "genre",
            "shelves",
        ]