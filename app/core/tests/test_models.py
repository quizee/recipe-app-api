from django.test import TestCase
from django.contrib.auth import get_user_model


class UserCreateTest(TestCase):

    def test_create_user(self):
        """Test creating a new user with an email is successful"""
        email = 'jeeyoon@gmail.com'
        password = 'jee123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_email_normalization(self):
        """Test the email for the new user is normalized"""
        email = 'jeeyoon@GMAIL.COM'
        password = 'jee123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email, email.lower())

    def test_invalid_email(self):
        """Test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(
                email=None,
                password='test123'
            )

    def test_super_user(self):
        """Test creating super user"""
        user = get_user_model().objects.create_superuser(
            email='admin',
            password='admin'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
