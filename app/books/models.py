from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    inventory = models.IntegerField(default=0)
    notes = models.ForeignKey('Note', on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    read = models.BooleanField(default=False)
    date_purchased =
    date_first_read =
    date_last_read =
    read_count = models.IntegerField(default=0)
    book_quotes = models.ForeignKey('Quote', on_delete=models.CASCADE)
    book_summary = models.TextField()
    favorite = models.BooleanField(default=False)
    isbn = models.CharField(max_length=20)
    # barcode =
    # similar_books
    # image =


class Category(models.Model):
    name = models.CharField(max_length=100)


class Note(models.Model):
    # user =
    date_created =
    date_updated =
    text = models.TextField()
    title = models.CharField(max_length=200)


class Quote(models.Model):
    # user =
    title = models.CharField(max_length=200)
    date_created =
    date_updated =
    author = models.CharField(max_length=100)
    text = models.TextField()
    page_found = models.IntegerField(default=0)
    favorite = models.BooleanField(default=False)
