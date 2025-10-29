from django.shortcuts import render
from .models import Book

def book_list(request):
    query = request.GET.get('author')
    books = Book.objects.all()

    if query:
        books = books.filter(author__username__icontains=query)

    return render(request, 'library/index.html', {'books': books, 'query': query})
