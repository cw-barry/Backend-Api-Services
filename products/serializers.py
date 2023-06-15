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
        fields = ("image", )


class ProductsSerializer(serializers.ModelSerializer):
    category =serializers.StringRelatedField()
    category_id = serializers.IntegerField()
    images = ImagesSerializer(many=True)

    class Meta:
        model = Products
        fields = ("id","category","category_id","title","price","description","images")

    def create(self, validated_data):
        images = validated_data.pop("images")
        # category = validated_data.pop("category_id")
        print(validated_data)

        product = Products.objects.create(**validated_data)
        # product = Products.objects.create(**validated_data, category=category.get("id"))

        for image in images:
            item = Images.objects.create(image, product=product)
            # item.product = product
            # item.save()

        return product

    def validate(self, data):
        print(type(data))
        return data

class BulkProductSerializer(serializers.Serializer):
    products = serializers.ListField()

    def create(self, validated_data):
        data = validated_data.pop("products")
        for item in data:
            images = item.pop("images")
            category = item.pop("category")
            item.pop("id")

            product = Products.objects.create(**item, category_id=category.get("id"))

            for image in images:
                Images.objects.create(image=image, product=product)
                # item.product = product
                # item.save()

        return {"products": data}



    
