from rest_framework import serializers

from app_books.serializers import BookSerializer
from .models import Readers, ReadersBooks


class ReadersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Readers
        fields = ["first_name", "last_name"]


class ReadersBooksSerializer(serializers.ModelSerializer):
    # reader = ReadersSerializer()
    # books = BookSerializer()

    class Meta:
        model = ReadersBooks
        fields = ["reader", "date_of_taking", "date_of_return", "delay", "books"]

    def update(self, instance, validated_data):
        instance.date_of_return = validated_data.get(
            "date_of_return", instance.date_of_return
        )
        if instance.date_of_return is not None:
            if instance.diff_date() > 7:
                instance.delay = True
            else:
                instance.delay = False
        instance.save()
        return instance
