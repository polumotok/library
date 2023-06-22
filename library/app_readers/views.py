from rest_framework import filters, viewsets
from rest_framework.permissions import IsAuthenticated

from .models import ReaderBook, LocationBook
from .serializers import ReadersBooksSerializer, LocationBookSerializer


class ReadersView(viewsets.ModelViewSet):
    queryset = ReaderBook.objects.all()
    serializer_class = ReadersBooksSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["reader__last_name", "reader__first_name", "books__title"]
    ordering_fields = ["reader__last_name", "reader__first_name", "books__title"]

class LocationBookView(viewsets.ModelViewSet):
    queryset = LocationBook.objects.all()
    serializer_class = LocationBookSerializer