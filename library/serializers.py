from rest_framework import serializers
from .models import categoryModel, subCategoryModel, authorsModel, booksModel, commentsModel

class categorySerializer(serializers.ModelSerializer):
    class Meta:
        model = categoryModel
        fields = '__all__'

class subCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = subCategoryModel
        fields = '__all__'

class authorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = authorsModel
        fields = '__all__'

class booksSerializer(serializers.ModelSerializer):
    class Meta:
        model = booksModel
        fields = '__all__'

class commentSerializer(serializers.ModelSerializer):
    class Meta:
        model = commentsModel
        fields = '__all__'


# Add similar serializers for Subcategory, Author, Book, and Comment