from django.urls import path
from .views import (
    CategoryListCreateView,
    SubCategoryListCreateView,
    BooksListCreateView,
    CommentsListCreateView,
    AuthorsListCreateView,
    BookListMostReadView,
    increase_book_views,
)

urlpatterns = [
    path('categories/', CategoryListCreateView.as_view(), name='category-list-create'),
    path('subcategories/', SubCategoryListCreateView.as_view(), name='subcategory-list-create'),
    path('books/', BooksListCreateView.as_view(), name='books-list-create'),
    path('comments/', CommentsListCreateView.as_view(), name='comments-list-create'),
    path('authors/', AuthorsListCreateView.as_view(), name='authors-list-create'),
    path('books/most-read/', BookListMostReadView.as_view(), name='books-most-read'),
    path('books/<int:book_id>/increase-views/', increase_book_views, name='increase-book-views'),
]
