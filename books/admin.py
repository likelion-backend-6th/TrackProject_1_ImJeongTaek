from django.contrib import admin

from books.models import Book, Rental


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'publisher', 'stock']


@admin.register(Rental)
class RentalAdmin(admin.ModelAdmin):
    list_display = ['user', 'get_book_title', 'rental_date', 'return_date']

    def get_book_title(self, obj):
        return obj.book.title

    get_book_title.short_description = 'Book Title'
