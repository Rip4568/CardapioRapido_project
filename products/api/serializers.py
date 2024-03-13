from rest_framework import serializers

from products.models import Product, ProductAddon, Category

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        
class ProductAddonSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductAddon
        fields = '__all__'