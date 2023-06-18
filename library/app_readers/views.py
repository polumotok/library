from rest_framework import filters, viewsets
from rest_framework.permissions import IsAuthenticated

from .models import  ReadersBooks
from .serializers import  ReadersBooksSerializer


class ReadersView(viewsets.ModelViewSet):
    queryset = ReadersBooks.objects.all()
    serializer_class = ReadersBooksSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["reader__last_name", "reader__first_name", "books__title"]
    ordering_fields = ["reader__last_name", "reader__first_name", "books__title"]
