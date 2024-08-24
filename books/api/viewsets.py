from rest_framework import viewsets 
from books.api import serializers
from books import models

class BooksViewSets(viewsets.ModelViewSet):
    serializer_class = serializers.BooksSerializer
    queryset = models.Books.objects.all()

class ImageViewSets(viewsets.ModelViewSet):
    serializer_class = serializers.ImageSerializer
    queryset = models.Image.objects.all()    