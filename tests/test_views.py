import json
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from restaurant.models import Menu, Booking


class MenuViewTest(TestCase):
    def setUp(self) -> None:
        # Add test instances of the Menu model
        Menu.objects.create(title="Menu 1", price=100, inventory=100)
        Menu.objects.create(title="Menu 2", price=200, inventory=200)

    def test_getall(self):
        #  Retrieve all Menu objects using API client
        client = APIClient()
        url = reverse("menu-item")
        response = client.get(url)

        # Assert the response status code
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Serialize the retrieved objects
        expected_data = [
            {"id": 2, "title": "Menu 1", "price": "100.00", "inventory": 100},
            {"id": 3, "title": "Menu 2", "price": "200.00", "inventory": 200},
        ]

        # Assert the serialized data equals the response
        self.assertEqual(json.loads(response.content), expected_data)
