from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")
    quantity = models.PositiveIntegerField(default=0)
    tags = models.CharField(max_length=200, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="products")
    date_added = models.DateTimeField(auto_now_add=True) 
    last_updated = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class ChangeLog(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="changes")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    change_type = models.CharField(max_length=50)  # e.g. "restock" or "sale"
    quantity_changed = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.change_type} of {self.product.name} by {self.user.username}"
