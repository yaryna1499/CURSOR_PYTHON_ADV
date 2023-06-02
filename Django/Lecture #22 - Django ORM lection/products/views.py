from django.shortcuts import render
from .models import Category, Product, ProductImage


from django.db.models import Q

def category_page(request, slug):
    category = Category.objects.get(slug=slug)
    
    sort_by = request.GET.get('sort_by')

    if sort_by == 'date_added':
        products = category.products.order_by('-date_added')
    elif sort_by == 'price':
        products = category.products.filter(
            Q(discount_price__isnull=False) | Q(price=0)
        ).order_by('discount_price', 'price')
    else:
        products = category.products.all()

    return render(request, "category.html", {"category": category, "products": products})





def product_page(request, id):
    product = Product.objects.get(id=id)
    return render(request, "product_page.html", {"product": product})