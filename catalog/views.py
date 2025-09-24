from django.shortcuts import render
from django.views import generic


from .models import Book, BookInstance, Author, Genre

def index(request):
    """View function for home page of site."""

    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    num_authors = Author.objects.count()

    num_genres = Genre.objects.count()

    the_in_title_count = Book.objects.filter(title__icontains='The').count()

    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1


    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_genres': num_genres,
        'num_visits': num_visits,
    }
    return render(
        request,
        'catalog/index.html', context=context
    )

class BookListView(generic.ListView):
    model = Book
    paginate_by = 3 
    context_object_name = 'book_list'
    queryset = Book.objects.all()
    template_name = 'catalog/books_list.html'

class BookDetailView(generic.DetailView):
    model = Book
    context_object_name = 'book'
    template_name = 'catalog/book_detail.html'

class AuthorListView(generic.ListView):
    model = Author 
    context_object_name = 'author_list'
    queryset = Author.objects.all().order_by('last_name')
    paginate_by = 3
    template_name = 'catalog/authors_list.html'

class AuthorDetailView(generic.DetailView):
    model = Author
    context_object_name = 'author'
    template_name = 'catalog/author_detail.html'

def about(request):
    return render(request, 'catalog/about.html')
