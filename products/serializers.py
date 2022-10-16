from unicodedata import category
from rest_framework import serializers
from .models import Category, Products, Images

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("id","name","image")

class ImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = ("name")


class ProductsSerializer(serializers.ModelSerializer):
    category =serializers.StringRelatedField()
    category_id = serializers.IntegerField()
    images = ImagesSerializer(many=True)

    class Meta:
        model = Products
        fields = ("id","category","category_id","title","price","description","images")

    def create(self, validated_data):
        images = validated_data.pop("images")
        category = validated_data.pop("category")

        product = Products.objects.create(**validated_data, category=category.get("id"))

        for image in images:
            item = Images.objects.create(image, product=item.product)
            # item.product = product
            # item.save()

        return product




    
