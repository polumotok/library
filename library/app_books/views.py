from rest_framework.permissions import IsAuthenticated

from .models import Books
from .serializers import BookSerializer
from rest_framework import filters, viewsets


class BooksViewSet(viewsets.ModelViewSet):
    queryset = Books.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["title", "author__last_name", "genre__title"]
    ordering_fields = ["title", "author__last_name", "genre__title"]
    ordering = ["title"]
