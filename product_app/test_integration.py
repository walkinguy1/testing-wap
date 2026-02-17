from django.test import TestCase
from django.urls import reverse
from product_app.models import Products


class ProductIntegrationTestCase(TestCase):

    def test_create_cheap_product(self):

        response = self.client.post(
            reverse("home"),
            {"name": "Cheap Product", "price": "50"}
        )

        self.assertEqual(response.status_code, 302)

        with self.assertRaises(Products.DoesNotExist):
            Products.objects.get(name="Cheap Product")
