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
            'isbn'
        )
