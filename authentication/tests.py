from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model

class UserAuthTests(APITestCase):

    def setUp(self):
        self.signup_url = reverse('signup')  
        self.login_url = reverse('login')      
        self.user_data = {
            'firstName': 'John',
            'lastName': 'Doe',
            'email': 'john.doe@example.com',
            'password': 'securepassword123',
        }

    def test_signup(self):
        response = self.client.post(self.signup_url, self.user_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['email'], self.user_data['email'])
        self.assertTrue(get_user_model().objects.filter(email=self.user_data['email']).exists())

    def test_login(self):
        # First, create a user
        self.client.post(self.signup_url, self.user_data)

        # Now try logging in
        response = self.client.post(self.login_url, {
            'email': self.user_data['email'],
            'password': self.user_data['password']
        })
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('token', response.data)  # Assuming you return a token on successful login
