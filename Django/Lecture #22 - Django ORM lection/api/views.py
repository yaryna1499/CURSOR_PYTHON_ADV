from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ProductSerializer, OrderSerializer
from products.models import Product, Category
from main.models import Order
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated


class ProductView(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        products = Product.objects.all()
        serialized_products = ProductSerializer(products, many=True)
        return Response(serialized_products.data)


class ProductSingleView(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get_object(self, id):
        try:
            product = Product.objects.get(id=id)
            return product
        except Product.DoesNotExist as e:
            return Response(str(e), status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        product = self.get_object(id)
        if product:
            serialized_product = ProductSerializer(product)
            return Response(serialized_product.data)
        return Response(None, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, id):
        product = self.get_object(id)
        if product:
            serialized_product = ProductSerializer(instance=product, data=request.data)
            if serialized_product.is_valid():
                serialized_product.save()
                return Response(serialized_product.data)
        return Response(None, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        product = self.get_object(id)
        if product:
            product.delete()
            return Response(None, status=status.HTTP_204_NO_CONTENT)
        return Response(None, status=status.HTTP_400_BAD_REQUEST)


class CategoryProductsView(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get_object(self, id):
        try:
            category = Category.objects.get(id=id)
            return category
        except Category.DoesNotExist as e:
            return Response(str(e), status=status.HTTP_404_NOT_FOUND)

    def get(self, request, category_id):
        category = self.get_object(category_id)
        if category and category.products.exists():
            products = ProductSerializer(category.products, many=True)
            return Response(products.data)
        return Response(None, status=status.HTTP_404_NOT_FOUND)


class OrderView(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        orders = Order.objects.all()
        serialized_orders = OrderSerializer(orders, many=True)
        return Response(serialized_orders.data)
