from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import categoryModel, subCategoryModel, authorsModel, booksModel, commentsModel
from .serializers import categorySerializer, subCategorySerializer, booksSerializer, commentSerializer

class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = categoryModel.objects.all()
    serializer_class = categorySerializer
    
class SubCategoryListCreateView(generics.ListCreateAPIView):
    queryset = subCategoryModel.objects.all()
    serializer_class = subCategorySerializer
    
class BooksListCreateView(generics.ListCreateAPIView):
    queryset = booksModel.objects.all()
    serializer_class = booksSerializer

class CommentsListCreateView(generics.ListCreateAPIView):
    queryset = commentsModel.objects.all()
    serializer_class = commentSerializer
    
class AuthorsListCreateView(generics.ListCreateAPIView):
    queryset = commentsModel.objects.all()
    serializer_class = commentSerializer

class BookListMostReadView(generics.ListAPIView):
    queryset = booksModel.objects.order_by('-views_count')[:10]  # Show top 10 most-read books
    serializer_class = booksSerializer

@api_view(['POST'])
def increase_book_views(request, book_id):
    try:
        book = booksModel.objects.get(id=book_id)
    except booksModel.DoesNotExist:
        return Response(status=404)

    book.views_count += 1
    book.save()
    return Response(status=200)
