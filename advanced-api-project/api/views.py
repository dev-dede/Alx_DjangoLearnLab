from rest_framework import generics, filters
from .serializers import BookSerializer
from .models import Book
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters import rest_framework

class BookFilter(rest_framework.FilterSet):
    title = rest_framework.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Book
        fields = ['title', 'publication_year']

class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    #filterset_fields = ['title', 'publication_year', 'author']
    filterset_class = BookFilter
    # Add DjangoFilterBackend even though it is set globally so as not to overide it
    filter_backends = [filters.OrderingFilter, rest_framework.DjangoFilterBackend]
    ordering_fields = ['title', 'publication_year']

class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

