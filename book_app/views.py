from django.shortcuts import render

# Create your views here.

def show_all_books(request):
    render(request, 'book_app/all_books.html')