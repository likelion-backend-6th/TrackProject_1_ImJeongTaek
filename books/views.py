from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect

from books.models import Book, Rental


def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books})


def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'books/book_detail.html', {'book': book})


def rent_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    if book.stock > 0:
        rental = Rental(user=request.user, book=book)
        rental.save()
        book.stock -= 1
        book.save()
        return redirect('books:book_detail', book_id)
    else:
        messages.error(request, f'{book.title} is no stock.')
        return redirect('books:book_list')


def return_book(request, rental_id):
    rental = Rental(user=request.user, id=rental_id)
    book = rental.book

    book.stock += 1
    book.save()
    return redirect('books:book_list')
