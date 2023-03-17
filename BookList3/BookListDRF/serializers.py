from rest_framework import serializers
from .models import Book
from decimal import Decimal


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
        # fields = ['id', 'title', 'author', 'price']


# class BookListSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     title = serializers.CharField(max_length=255)
#     author = serializers.CharField(max_length=255)
#     price = serializers.DecimalField(max_digits=5, decimal_places=2)

# class CategorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Category
#         fields = '__all__'


class BookListSerializer(serializers.ModelSerializer):
    # max_price=serializers.IntegerField(source='price')
    max_price = serializers.DecimalField(
        source='price', max_digits=5, decimal_places=2)
    price_after_gst = serializers.SerializerMethodField(
        method_name='calculate_price')
    
    # category=serializers.StringRelatedField()
    # category=CategorySerializer()

    class Meta:
        model = Book
        # fields='__all__'
        fields = ['id', 'title', 'author', 'max_price', 'price_after_gst',]

    def calculate_price(self, product: Book):
        return round(product.price*Decimal(1.18), 2)
