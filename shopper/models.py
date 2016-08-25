from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Shopper(models.Model):
    user = models.OneToOneField(User)


class ShoppingList(models.Model):
    shopper = models.ForeignKey(Shopper, on_delete=models.CASCADE,
                                related_name='list')
    title = models.CharField(max_length=100)
    budget = models.IntegerField()

class ShoppingItem(models.Model):
    shopping_list = models.ForeignKey(ShoppingList, on_delete=models.CASCADE,
                                      related_name='items')
    item_name = models.CharField(max_length=100)
    shopper = models.OneToOneField(Shopper)
