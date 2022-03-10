from . import views
from django.urls import path

urlpatterns = [
    path('', views.show_all_books),
    path('book/<int:id_book>', views.show_one_book),
]
