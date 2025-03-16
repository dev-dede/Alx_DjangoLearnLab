from rest_framework import serializers
from .models import Book, Author
from django.utils import timezone

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"
    
    def validate_publication_year(self, value):
        """
        Ensure the publication year is not in the future.
        """
        if value > timezone.now().year:
            raise serializers.ValidationError("Publication date can not be in the future")
        return value
        

class AuthorSerializer(serializers.ModelSerializer):
    book = BookSerializer() # Nested serializer for the related book

    class Meta:
        model = Author
        fields = ['name', 'book']