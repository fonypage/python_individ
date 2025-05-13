from django.urls import path
from . import views

app_name = 'library'

urlpatterns = [
    path('',                  views.BookListView.as_view(),   name='book_list'),
    path('book/add/',         views.BookCreateView.as_view(), name='book_add'),
    path('book/<int:pk>/',    views.BookDetailView.as_view(), name='book_detail'),
    path('book/<int:pk>/edit/', views.BookUpdateView.as_view(), name='book_edit'),
]
