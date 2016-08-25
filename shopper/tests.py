from django.test import TestCase, Client
from django.contrib.auth.models import User
from models import Shopper, ShoppingItem, ShoppingList
from django.urls import reverse

# Create your tests here.
class ShopperModelTest(TestCase):
    def test_shopper_creation(self):
        user = User.objects.create(username='kiura',
                                   email='kiuraalex@gmail.com',
                                   password='password')
        shopper = Shopper.objects.create(user=user)
        shopping_list = ShoppingList.objects.create(shopper=shopper, title='today',
                                               budget=5000)
        shopping_item = ShoppingItem(shopper=shopper, item_name='soap',
                                     shopping_list=shopping_list)
        shopping_item.save()

        # test shopper was created
        first_shopper = Shopper.objects.all()[0]
        self.assertEqual(len(Shopper.objects.all()), 1)
        # test shoppers attributes
        self.assertEqual(shopper.user.username, first_shopper.user.username)
        self.assertEqual(shopper.user.email, first_shopper.user.email)

        self.assertEqual(len(ShoppingList.objects.all()), 1)
        # test shopping list attributes
        first_shopping_list = ShoppingList.objects.all()[0]
        self.assertEqual(first_shopping_list.title, shopping_list.title)
        self.assertEqual(first_shopping_list.budget, shopping_list.budget)
        self.assertEqual(len(first_shopping_list.items.all()), 1)

        self.assertEqual(first_shopping_list.items.all()[0].item_name,
                         shopping_item.item_name)

class ShopperViewTest(TestCase):
    def test_view_with_no_shopping_list(self):
        response = self.client.get(reverse('shopper'))
