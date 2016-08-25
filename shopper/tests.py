from django.test import TestCase
from django.contrib.auth.models import User
from models import Shopper, ShoppingItem, ShoppingList

# Create your tests here.
class ShopperTest(TestCase):
    def test_shopper_creation(self):
        user = User.objects.create(name='kiura',
                                   email='kiuraalex@gmail.com',
                                   password='password')
        shopper = Shopper.objects.create(user=user)
        shopping_list = Shopper.objects.create(user=user, title='today',
                                               budget=5000)
        shopping_item = ShoppingItem(shopper=shopper, item_name='soap',
                                     shopping_list=shopping_list)
        shopping_item.save()

        # test shopper was created
        first_shopper = Shopper.objects.all()[0]
        self.assertEqual(len(Shopper.objects.all()), 1)
        # test shoppers attributes
        self.assertEqual(shopper.user.name, first_shopper.user.name)
        self.assertEqual(shopper.user.email, first_shopper.user.email)

        self.assertEqual(len(ShoppingList.objects.all()), 1)
        # test shopping list attributes
        first_shopping_list = ShoppingList.objects.all()[0]
        self.assertEqual(first_shopping_list.title, shopping_list.title)
        self.assertEqual(first_shopping_list.budget, shopping_list.budget)
        self.assertEqual(len(first_shopping_list.items), 1)

        self.assertEqual(len(first_shopping_list.items[0].item_name),
                         shopping_item.item_name)
