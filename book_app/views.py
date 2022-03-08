from django.shortcuts import render
from .models import Book

# Create your views here.

def show_all_books(request):
    books = Book.objects.all()
    data = {
        'books': books
    }
    return render(request, 'book_app/all_books.html', context=data)