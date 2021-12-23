from django.urls import path
from .views import (
    BookListView, BookDetailView, BookCreateView, 
    BookUpdateView, BookDeleteView, AuthorBookListView,
)
from . import views

urlpatterns = [
path('home_httpresponse/', views.home_httpresponse, name='yapp-home-httpresponse'),
path('about_httpresponse/', views.about_httpresponse, name='yapp-about-httpresponse'),
path('home_render/', views.home_render, name='yapp-home-render'), 
path('about_render/', views.about_render, name='yapp-about-render'), 
path('about/', views.about, name='yapp-about'),
path('', BookListView.as_view(), name='yapp-home'),
path('book/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
path('book/new/', BookCreateView.as_view(), name='book-create'),
path('book/<int:pk>/update', BookUpdateView.as_view(), name='book-update'),
path('book/<int:pk>/delete', BookDeleteView.as_view(), name='book-delete'),
path('author/<str:author>/', AuthorBookListView.as_view(), name='author-booklist'),
]