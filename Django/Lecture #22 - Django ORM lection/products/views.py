from django.shortcuts import render
from .models import Category, Product, ProductImage


def category_page(request, slug):
    category = Category.objects.get(slug=slug)
    return render(request, "category.html", {"category": category, "products": category.products.all()})


def product_page(request, id):
    product = Product.objects.get(id=id)
    return render(request, "product_page.html", {"product": product})