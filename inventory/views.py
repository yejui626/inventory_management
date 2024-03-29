from .models import Supplier, Book
from .serializers import BookSerializer
from rest_framework.generics import ListAPIView,RetrieveAPIView,CreateAPIView,DestroyAPIView,UpdateAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework import status,viewsets,filters
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend


class BookList(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]
    filterset_fields = ['category', 'author']
    search_fields = ['title']
    ordering_fields = ['price', 'category']
    ordering = ['title']


class BookDetail(RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)


class AddBook(CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class DeleteBook(DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_url_kwarg = 'pk'

class UpdateBook(UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_url_kwarg = 'pk'

