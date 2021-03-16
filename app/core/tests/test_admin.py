from django.test import TestCase, Client
# make test requests to our application in our unit tests
from django.contrib.auth import get_user_model
from django.urls import reverse
# generate urls for our django admin page


class AdminSiteTest(TestCase):
    def setUp(self):  # will be run before every test that we run
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='admin@gmail.com',
            password='admin'
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email='user@gmail.com',
            password='user',
            name='user name'
        )

    def test_users_listed(self):
        """test that users listed in admin page"""
        url = reverse('admin:core_user_changelist')
        # app name and the url that you want
        res = self.client.get(url)

        self.assertContains(res, self.user.name)
        # check if the response contains specific field
        self.assertContains(res, self.user.email)
        # and it is smart enough to check if status_code is 200 by default

    def test_users_changed(self):
        """test that user edit page works"""
        url = reverse('admin:core_user_change', args=[self.user.id])
        # admin/core/user/1 id is passed to the url like this
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)

    def test_create_user_page(self):
        """test that the create user page works"""
        url = reverse('admin:core_user_add')
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)
