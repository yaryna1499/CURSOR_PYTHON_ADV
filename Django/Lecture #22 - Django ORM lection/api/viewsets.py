from rest_framework import viewsets
from products.models import Product, Category
from main.models import Order
from .serializers import ProductSerializer, CategorySerializer, OrderSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
