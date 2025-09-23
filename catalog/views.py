from django.shortcuts import render
from .models import Book, BookInstance, Author, Genre

def index(request):
    """View function for home page of site."""

    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    num_authors = Author.objects.count()

    num_genres = Genre.objects.count()

    the_in_title_count = Book.objects.filter(title__icontains='The').count()



    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_genres': num_genres,
        'the_in_title_count': the_in_title_count,
    }
    return render(
        request,
        'catalog/index.html', context=context
    )

def books_list_view(request):
    books = Book.objects.all()
    return render(request, 'catalog/books_list.html', {'books': books})

def authors_list_view(request):
    authors = Author.objects.all()
    return render(request, 'catalog/authors_list.html', {'authors': authors})

def about(request):
    return render(request, 'catalog/about.html')
