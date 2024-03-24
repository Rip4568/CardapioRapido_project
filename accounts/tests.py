from django.test import TestCase
from .models import User

class TestUser(TestCase):
    def setUp(self) -> None:
        self.user = User.objects.create_user(
            username='test',
            email='email@test.com',
            password='123456',
            phone_number='415251521'
        )
        
    def test_user_creation(self):
        self.assertEqual(self.user.username, 'test')
        self.assertEqual(self.user.email, 'email@test.com')
        self.assertEqual(self.user.is_active, True)
        self.assertEqual(self.user.is_staff, False)
        self.assertEqual(self.user.is_superuser, False)
        self.assertEqual(self.user.groups.count(), 0)
        self.assertEqual(self.user.user_permissions.count(), 0)
        self.assertEqual(self.user.get_username(), 'test')
        self.assertEqual(self.user.get_email(), 'email@test.com')
        self.assertEqual(self.user.get_password(), '123456')
        
    def test_create_superuser(self):
        self.user = User.objects.create_superuser(
            username='test',
            email='email@test.com',
            password='<PASSWORD>',
            phone_number='415251521'
        )
        self.assertEqual(self.user.username, 'test')
        self.assertEqual(self.user.email, 'email@test.com')
        self.assertEqual(self.user.is_active, True)
        self.assertEqual(self.user.is_staff, True)
        self.assertEqual(self.user.is_superuser, True)
        self.assertEqual(self.user.groups.count(), 0)
        self.assertEqual(self.user.user_permissions.count(), 0)
        self.assertEqual(self.user.get_full_name(), 'test')
        self.assertEqual(self.user.get_short_name(), 'test')
        self.assertEqual(self.user.get_username(), 'test')