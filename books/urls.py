from django.urls import path

from books import views

app_name = 'books'

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('books/<book_id>/', views.book_detail, name='book_detail'),
    path('my_rentals/', views.return_book, name='rent_book'),
]