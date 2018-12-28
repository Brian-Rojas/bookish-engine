from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *

class BookView(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
