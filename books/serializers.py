#DRF
from rest_framework import serializers
from .models import Book, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug']

class BookSerializer(serializers.ModelSerializer):
    seller = serializers.ReadOnlyField(source='seller.username')
    category_name = serializers.ReadOnlyField(source='category.name')

    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'category', 'category_name', 'condition',
                  'price', 'description', 'image', 'thumbnail', 'seller', 'status', 'posted_at']
        read_only_fields = ['seller', 'status', 'posted_at']