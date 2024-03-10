from os import name
import pdb
from django.db.models import Sum
from django.test import TestCase
from accounts.models import User
from core.tests import TestCaseColorFull
from orders.models import Cart, CartItem, Order, OrderItem, OrderItemAddon, Payment
from products.models import Category, Product, ProductAddon
from stores.models import Store

class TestCartAndStore(TestCaseColorFull):
    def setUp(self) -> None:
        """ O método setUp cria um usuário dono da loja, uma loja, um usuário comprador 
        e um carrinho associado a essa loja e comprador. """
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
        self.category = Category.objects.create(
            name="Test Category",
            store=self.store
        )

    def test_create_cart(self):
        """ O método test_create_cart verifica se o carrinho 
        foi criado corretamente com o usuário comprador e a loja associados. """
        self.assertEqual(self.cart.user, self.buyer)
        self.assertEqual(self.cart.store, self.store)

    def test_store_slug(self):
        """ O método test_store_slug verifica se o slug da loja
        foi gerado corretamente a partir do nome da loja. """
        self.assertEqual(self.store.slug, "store-test")

    def test_create_product(self):
        """ O método test_create_product cria um produto 
        para a loja e verifica se o produto foi criado com sucesso. """
        product = Product.objects.create(
            name="Test Product",
            store=self.store,
            category=self.category,
            price=10.99
        )
        self.assertIsNotNone(product.pk)

    def test_create_cart_item(self):
        """ O método test_create_cart_item cria um item no carrinho 
        para um produto e verifica se a quantidade e o preço total 
        foram calculados corretamente. """
        product = Product.objects.create(
            name="Test Product",
            store=self.store,
            category=self.category,
            price=10.99
        )
        cart_item = CartItem.objects.create(
            cart=self.cart,
            product=product,
            quantity=2
        )
        self.assertEqual(cart_item.quantity, 2)
        self.assertEqual(cart_item.total_price, 21.98)

    def test_create_order(self):
        """ O método test_create_order cria um pedido para o usuário 
        comprador e a loja, e verifica se o pedido foi criado com o status correto. """
        order = Order.objects.create(
            user=self.buyer,
            store=self.store,
            status=Order.Status.PENDING
        )
        self.assertEqual(order.user, self.buyer)
        self.assertEqual(order.store, self.store)
        self.assertEqual(order.status, Order.Status.PENDING)

    def test_create_order_item(self):
        """ O método test_create_order_item cria um item de pedido 
        para um produto e verifica se a quantidade e o preço total 
        foram calculados corretamente. """
        product = Product.objects.create(
            name="Test Product",
            store=self.store,
            category=self.category,
            price=10.99
        )
        order = Order.objects.create(
            user=self.buyer,
            store=self.store,
            status=Order.Status.PENDING
        )
        order_item = OrderItem.objects.create(
            order=order,
            product=product,
            price=product.price,
            original_price=product.price,
            quantity=2
        )
        self.assertEqual(order_item.quantity, 2)
        self.assertEqual(order_item.total_price, 21.98)

    def test_create_order_item_addon(self):
        """ O método test_create_order_item_addon cria um adicional 
        para um item de pedido e verifica se o adicional foi criado corretamente. """
        product = Product.objects.create(
            name="Hamburger",
            store=self.store,
            category=self.category,
            price=10.99
        )
        addon = ProductAddon.objects.create(
            name="Extra Cheese",
            category=self.category,
            price=2.99
        )
        order = Order.objects.create(
            user=self.buyer,
            store=self.store,
            status=Order.Status.PENDING
        )
        order_item = OrderItem.objects.create(
            order=order,
            product=product,
            price=product.price,
            original_price=product.price,
            quantity=2
        )
        order_item_addon = OrderItemAddon.objects.create(
            order=order,
            product_addon=addon,
            quantity=2
        )
        total_quantity_order_items:float = order.items.all().aggregate(
            Sum('quantity')
        )['quantity__sum']
        
        total_quantity_order_items_addon:float = order.addons.all().aggregate(
            Sum('quantity')
        )['quantity__sum']
        self.assertEqual(order_item_addon.quantity, 2)
        self.assertEqual(order_item_addon.total_price, 5.98)
        self.assertEqual(total_quantity_order_items, 2)
        self.assertEqual(total_quantity_order_items_addon, 2)

    def test_create_payment(self):
        """ O método test_create_payment cria um pagamento 
        para um pedido e verifica se o pagamento foi criado com os dados corretos. """
        order = Order.objects.create(
            user=self.buyer,
            store=self.store,
            status=Order.Status.PENDING
        )
        payment = Payment.objects.create(
            order=order,
            amount=20.99,
            payment_method="credit",
            status="pending"
        )
        self.assertEqual(payment.order, order)
        self.assertEqual(payment.amount, 20.99)
        self.assertEqual(payment.payment_method, "credit")
        self.assertEqual(payment.status, "pending")