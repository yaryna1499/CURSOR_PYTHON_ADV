from django.db import models
from django.db.models import Q
from django import utils
from django.contrib.auth.models import User


class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.IntegerField(null=False)
    discount_price = models.IntegerField(null=True, blank=True)
    show_on_main_page = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_added = models.DateTimeField(default=utils.timezone.now)

    @property
    def main_image(self):
        return (
            ProductImage.objects.filter(Q(product_id=self.id) & Q(is_main=True))
            .first()
            .image
        )

    @property
    def all_images(self):
        product_images = ProductImage.objects.filter(product_id=self.id)
        image_list = [product_image.image for product_image in product_images]
        return image_list

    def __str__(self):
        return str(self.id) + " " + self.title


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="uploads/products/")
    is_main = models.BooleanField(default=False)

    class Meta:
        unique_together = ("product", "is_main")

    def __str__(self):
        return str(self.product.id) + " " + self.product.title + "|" + str(self.id)


class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.CharField(max_length=255, unique=True, default="slug")
    parent = models.ForeignKey(
        "Category", null=True, blank=True, on_delete=models.PROTECT
    )
    products = models.ManyToManyField(Product)

    def __str__(self):
        return self.title
    

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="comments")
    parent = models.ForeignKey("Comment", default=None, null=True, on_delete=models.CASCADE, related_name="childs")
    text = models.TextField()

    @property
    def child_comments(self):
        return self.childs.all()

    def __str__(self):
        return self.text
