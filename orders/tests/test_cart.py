from django.test import TestCase
from accounts.models import User
from core.tests import TestCaseColorFull
from orders.models import Cart, CartItem, Order, OrderItem, OrderItemAddon, Payment, CartItemAddon
from products.models import Product, ProductAddon
from stores.models import Store


class TestCartAndStore(TestCaseColorFull):
    def setUp(self) -> None:
        self.owner = User.objects.create_user(
            email="ownerTest@gmail.com",
            password="123456",
            username="ownerTest",
            phone_number="1234567890"
            )
        self.store = Store.objects.create(
            name="Store Test",
            user=self.owner
            )
        
        self.buyer = User.objects.create_user(
            email="buyerTest@gmail.com",
            password="123456",
            username="buyerTest",
            phone_number="12345678901"
            )
        self.cart = Cart.objects.create(
            user=self.buyer,
            store=self.store
        )

    def test_create_cart(self):
        self.assertEqual(self.cart.user, self.buyer)
        
    def test_store_slug(self):
        self.assertEqual(self.store.slug, "store-test")