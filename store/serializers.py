from rest_framework import serializers
from store.models import Product, Collection
from decimal import Decimal


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ['id', 'title','products_count']

    products_count = serializers.IntegerField()

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id','title', 'slug', 'inventory', 'unit_price','description','price_with_tax' ,'collection']
   
    price_with_tax = serializers.SerializerMethodField(method_name='calculate_tax')

    def calculate_tax(self,product: Product):
        return product.unit_price * Decimal(1.1)

    