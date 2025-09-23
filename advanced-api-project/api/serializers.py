from rest_framework import serializers
from .models import Author, Book

# Serializer for Book model
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']

    # Example of custom validation for publication_year
    def validate(self, data):
        if data['publication_year'] > 2025:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return data

# Serializer for Author model with nested books
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']