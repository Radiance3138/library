from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('books-list/', views.books_list_view, name='books_list'),
    path('authors-list/', views.authors_list_view, name='authors_list'),
]