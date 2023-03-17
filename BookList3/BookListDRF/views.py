from django.shortcuts import render
from .models import Book
from .serializers import BookSerializer, BookListSerializer
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
# Create your views here.


class BookView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class SingleBookView(generics.RetrieveUpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


# @api_view()
# def books(request):
#     books = Book.objects.all()
#     return Response(books.values())


@api_view()
def all_books(request):
    books = Book.objects.all()
    # books = Book.objects.select_related('category').all()
    serialized_item = BookListSerializer(books, many=True)
    return Response(serialized_item.data)


@api_view()
def single_book(request, pk):
    # books = Book.objects.get(pk=pk)
    book = get_object_or_404(Book, pk=pk)
    serialized_item = BookListSerializer(book)
    return Response(serialized_item.data)
