from rest_framework import serializers
from products.models import Product, Category
from main.models import Order
from PIL import Image
import tempfile


import base64


def get_image(image_path):
    with open(image_path, "rb") as image_file:
        image_data = image_file.read()
        encoded_image = base64.b64encode(image_data)
        return encoded_image.decode("utf-8")


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    image_field = serializers.SerializerMethodField()

    def get_image_field(self, product):
        image_path = "media/" + str(product.main_image)
        image_data = get_image(image_path)
        return image_data

    class Meta:
        model = Product
        fields = [
            "id",
            "title",
            "description",
            "price",
            "discount_price",
            "image_field",
        ]


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    products = ProductSerializer(read_only=True, many=True)

    class Meta:
        model = Category
        fields = ["id", "title", "slug", "products"]


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Order
        fields = [
            "id",
            "first_name",
            "last_name",
            "address",
            "email",
            "total_price",
            "code",
        ]
