from django.urls import path
from . import views

# TODO: create views for language-detail and language-detail/<int=pk> to pass test
# TODO: create views for genre-detail and genre-detail/<int=pk> to pass test

urlpatterns = [
    # standard urls
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    # book urls
    path('books/', views.BookListView.as_view(), name='books'),
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
    path('mybooks/', views.LoanedBooksByUserListView.as_view(),name='my-borrowed'),
    # author urls
    path('authors/', views.AuthorListView.as_view(), name='authors'),
    path('author/<int:pk>', views.AuthorDetailView.as_view(), name='author-detail'),
    # genre urls
    # path('genres/', views.GenreListView.as_view(), name='genres'),
    # path('genre/<int:pk>', views.GenreDetailView.as_view(), name='genre-detail'),
    # language urls
    # path('languages/', views.LanguageListView.as_view(), name='languages'),
    # path('language/<int:pk>', views.LanguageDetailView.as_view(), name='language-detail'),
    # staff urls
    path('book/create/', views.BookCreate.as_view(), name= 'book-create'),
    path('book/<int:pk>/update/', views.BookUpdate.as_view(), name='book-update'),
    path('book/<int:pk>/delete/', views.BookDelete.as_view(), name='book-delete'),
    path('borrowed/', views.LoanedBooksByUsersListView.as_view(), name='all-borrowed'),
    path('book/<uuid:pk>/renew/', views.renew_book_librarian, name='renew-book-librarian'),
    path('author/create/', views.AuthorCreate.as_view(), name= 'author-create'),
    path('author/<int:pk>/update/', views.AuthorUpdate.as_view(), name='author-update'),
    path('author/<int:pk>/delete/', views.AuthorDelete.as_view(), name='author-delete'),
]