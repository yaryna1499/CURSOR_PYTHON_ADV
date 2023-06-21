from django.shortcuts import render, HttpResponseRedirect, redirect
from .models import Category, Product, Comment

from django.db.models import Q


def category_page(request, slug):
    category = Category.objects.get(slug=slug)

    sort_by = request.GET.get("sort_by")

    if sort_by == "date_added":
        products = category.products.order_by("-date_added")
    elif sort_by == "price":
        products = category.products.filter(
            Q(discount_price__isnull=False) | Q(price=0)
        ).order_by("discount_price", "price")
    else:
        products = category.products.all()

    return render(
        request, "category.html", {"category": category, "products": products}
    )


def product_page(request, id):
    product = Product.objects.get(id=id)
    comments = Comment.objects.filter(parent_id=None).filter(product_id=product.id)
    return render(request, "product_page.html", {"product": product, "comments": comments})




def add_comment(request, product_id):
    if request.user.is_authenticated:
        if request.method == "POST":
            comment = Comment()
            comment.user = request.user
            comment.product_id = product_id
            comment.text = request.POST.get("comment-text")
            if request.POST.get("parent", False):
                comment.parent_id = int(request.POST.get("parent"))
            comment.save()
            return redirect("product_page", id=str(product_id))
    return HttpResponseRedirect("/")
