from django.db import models
from django.contrib.auth import get_user_model

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100, null=True)
    inventory = models.IntegerField(default=0)
    notes = models.ForeignKey('Note', on_delete=models.CASCADE, null=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True)
    read = models.BooleanField(default=False)
    date_purchased = models.DateField(auto_now=False, auto_now_add=False, null=True)
    date_first_read = models.DateField(auto_now=False, auto_now_add=False, null=True)
    date_last_read = models.DateField(auto_now=False, auto_now_add=False, null=True)
    date_added = models.DateTimeField(auto_now=False, auto_now_add=True)
    read_count = models.IntegerField(default=0)
    book_quotes = models.ForeignKey('Quote', on_delete=models.CASCADE, null=True)
    book_summary = models.TextField(null=True)
    favorite = models.BooleanField(default=False)
    ISBN = models.CharField(max_length=20, null=True)
    # similar_books =
    # image =

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Note(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now=False, auto_now_add=True)
    date_updated = models.DateField(auto_now=True, auto_now_add=False)
    text = models.TextField()
    title = models.CharField(max_length=200, null=True)


class Quote(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    title = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now=False, auto_now_add=True)
    date_updated = models.DateField(auto_now=True, auto_now_add=False)
    author = models.CharField(max_length=100, null=True)
    text = models.TextField()
    page_found = models.IntegerField(default=0)
    favorite = models.BooleanField(default=False)
