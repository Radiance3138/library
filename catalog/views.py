from django.shortcuts import render

def index(request):
    """View function for home page of site."""

    context = {
        'title': 'Home',
        'header': 'Hello, World!',
    }
    return render(
        request,
        'catalog/index.html', context=context
    )

# Create your views here.
