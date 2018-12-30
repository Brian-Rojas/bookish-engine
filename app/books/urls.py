from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('books', views.BookView)
router.register('notes', views.NoteView)
router.register('category', views.CategoryView)
router.register('quotes', views.QuoteView)

urlpatterns = [
    path('', include(router.urls))
]
