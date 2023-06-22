from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Book, Author, Genre
from .serializers import BookSerializer
from rest_framework import filters, viewsets


class BooksViewSet(viewsets.ModelViewSet):
    """
    Класс позволяет добавлять, изменять, удалять книги
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["title", "author__last_name", "genre__title"]
    ordering_fields = ["title", "author__last_name", "genre__title"]
    ordering = ["title"]

    def create(self, request, *args, **kwargs):
        """
        Функция позволяет добавить новую книгу

        book - добавляет новую книгу
        authors - добавляет авторов к новой книге
        genres - добавляет жанры к новой книге
        """
        book = Book.objects.create(
            title=request.data["title"],
            publication=request.data["publication"],
        )
        book.save()

        authors = Author.objects.in_bulk(request.data["authors"])
        for author in authors:
            book.authors.add(Author.objects.get(id=author))

        genres = Genre.objects.in_bulk(request.data["genres"])
        for genre in genres:
            book.genres.add(Genre.objects.get(id=genre))

        serializer = BookSerializer(book)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        """
        Функция  обновляет информацию о книге, авторах, жанрах
        """
        book = Book.objects.get(
            id=request.data["id"],
        )
        book.title = request.data["title"]
        book.publication = request.data["publication"]
        book.save()

        authors = Author.objects.in_bulk(request.data["authors"])
        book.authors.clear()
        for author in authors:
            book.authors.add(Author.objects.get(id=author))

        genres = Genre.objects.in_bulk(request.data["genres"])
        book.genres.clear()
        for genre in genres:
            book.genres.add(Genre.objects.get(id=genre))

        serializer = BookSerializer(book)
        return Response(serializer.data)
