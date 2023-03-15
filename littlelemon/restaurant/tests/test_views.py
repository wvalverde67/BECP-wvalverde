from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer
from django.contrib.auth.models import User

class MenuViewTest(TestCase):

    def setUp(self):
        # Create a user
        self.user = User.objects.create_user(username='admindjango', password='employee@123!')

        # Set up the test client
        self.client = APIClient()

        # Authenticate the test client
        self.client.force_authenticate(user=self.user)

        # Add a few test instances of the Menu model
        self.menu1 = Menu.objects.create(title="IceCream", price=80, inventory=100)
        self.menu2 = Menu.objects.create(title="Pizza", price=200, inventory=50)
        self.menu3 = Menu.objects.create(title="Pasta", price=150, inventory=30)

    def test_getall(self):
        # Get the URL for the MenuItemsView
        url = reverse('menu_items_view')

        # Send a GET request to the URL
        response = self.client.get(url)

        # Retrieve all the Menu objects
        menus = Menu.objects.all()

        # Serialize the objects
        serializer = MenuSerializer(menus, many=True)

        # Check if the serialized data equals the response
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)