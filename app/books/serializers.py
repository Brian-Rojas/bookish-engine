from rest_framework import serializers
from .models import *

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = (
            'title',
            'author',
            'inventory',
            'notes',
            'category',
            'read',
            'date_purchased',
            'date_first_read',
            'date_last_read',
            'date_added',
            'read_count',
            'book_quotes',
            'book_summary',
            'favorite',
            'ISBN'
        )


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'name',
        )


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = (
            'user',
            'book',
            'date_created',
            'date_updated',
            'note',
            'title'
        )


class QuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quote
        fields = (
            'user',
            'title',
            'date_created',
            'date_updated',
            'author',
            'text',
            'page_found',
            'favorite'
        )
