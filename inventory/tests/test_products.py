from django.test import TestCase
from rest_framework.test import APIClient
from .models import Product, Category

class ProductTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.category = Category.objects.create(name="Electronics")
        self.product = Product.objects.create(
            name="Laptop", category=self.category, quantity=10
        )

    def test_list_products(self):
        response = self.client.get('/api/products/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

    def test_create_product(self):
        response = self.client.post('/api/products/', {
            "name": "Phone",
            "category": self.category.id,
            "quantity": 5
        }, format='json')
        self.assertEqual(response.status_code, 201)
