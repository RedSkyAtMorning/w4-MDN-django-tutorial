from django.contrib import admin
from django.urls import path
from catalog.views import BookListView, BookDetailView


urlpatterns = [
    path('', views.index, name='index'),
    path( 'books/', views.BookListView.as_view(), name = 'books'),
    path('books/<int:pk>', views.BookDetailView.as_view(), name = 'book-detail'),
    ]
