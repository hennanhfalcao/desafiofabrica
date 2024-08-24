from rest_framework import serializers
from books import models

class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Books
        fields = '__all__'

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Image
        fields = "__all__"
