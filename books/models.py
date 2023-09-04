from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    publisher = models.CharField(max_length=200)
    stock = models.PositiveIntegerField()
    summary = models.TextField(blank=True)

    def __str__(self):
        return self.title


class Rental(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='books')
    rental_date = models.DateField(auto_now_add=True)
    return_date = models.DateField(default=timezone.now() + timezone.timedelta(days=7))

    class Meta:
        ordering = ['rental_date']
