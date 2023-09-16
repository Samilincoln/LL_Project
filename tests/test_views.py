'''
from django.test import TestCase
from restaurant.views import MenuItemView

class menuitemview(TestCase):
    def setup(self):
        item = MenuItemView.queryset.get_or_create(title='IceCream',price=80,inventory=100)
        itemview = item.test_get()

        self.assertEqual(itemview,'IceCream : 80')
'''
    