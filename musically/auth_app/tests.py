from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from musically.auth_app.forms import RegisterUserForm, LoginUserForm
from .views import RegisterUserView, LoginUserView, LogoutUserView, ProfileDetailView, ProfileDeleteView


class AuthAppTestCase(TestCase):
    def setUp(self):
        self.user_data = {
            'username': 'testuser',
            'password': 'testpassword'
        }
        self.user = get_user_model().objects.create_user(**self.user_data)


    def test_login_user_view(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'common/login.html')

        response = self.client.post(reverse('login'), data=self.user_data)
        self.assertEqual(response.status_code, 302)  # Redirect on successful login

    def test_logout_user_view(self):
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 302)  # Redirect on logout
        self.assertRedirects(response, reverse('start page'))


