# from django.urls import reverse
# from rest_framework import status
# from rest_framework.test import APITestCase
# from django.contrib.auth import get_user_model

# class UserAuthTests(APITestCase):

#     def setUp(self):
#         self.signup_url = reverse('signup')  
#         self.login_url = reverse('login')      
#         self.user_data = {
#             'firstName': 'John',
#             'lastName': 'Doe',
#             'email': 'john.doe@example.com',
#             'password': 'securepassword123',
#         }

#     def test_signup(self):
#         response = self.client.post(self.signup_url, self.user_data)
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         self.assertEqual(response.data['email'], self.user_data['email'])
#         self.assertTrue(get_user_model().objects.filter(email=self.user_data['email']).exists())

#     def test_login(self):
#         # First, create a user
#         self.client.post(self.signup_url, self.user_data)

#         # Now try logging in
#         response = self.client.post(self.login_url, {
#             'email': self.user_data['email'],
#             'password': self.user_data['password']
#         })
        
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertIn('token', response.data)  # Assuming you return a token on successful login


# from django.test import TestCase, override_settings
# from django.core.mail import send_mail
# from django.core.mail.backends.locmem import EmailBackend

# class EmailTest(TestCase):
#     @override_settings(
#         EMAIL_BACKEND='django.core.mail.backends.locmem.EmailBackend',  # Use in-memory backend
#         EMAIL_HOST='smtp.gmail.com',
#         EMAIL_PORT=587,
#         EMAIL_USE_TLS=True,
#         EMAIL_HOST_USER='antrixphotosonam@gmail.com',
#         EMAIL_HOST_PASSWORD='photos12345',
#     )
#     def test_send_email(self):
#         # Send test email
#         response = send_mail(
#             subject="Test Email",
#             message="This is a test email.",
#             from_email="antrixphotosonam@gmail.com",
#             recipient_list=["antrikshsaini96@gmail.com"],
#         )

#         # Assert email was sent successfully
#         self.assertEqual(response, 1)  # send_mail returns the number of emails sent

#         # Assert email content in Django test email outbox
#         from django.core.mail import outbox
#         self.assertEqual(len(outbox), 1)  # Ensure one email was sent
#         self.assertEqual(outbox[0].subject, "Test Email")
#         self.assertEqual(outbox[0].body, "This is a test email.")
#         self.assertEqual(outbox[0].to, ["antrikshsaini96@gmail.com"])


from django.test import TestCase
from django.core.mail import send_mail
import smtplib

class RealEmailTest(TestCase):
    def test_send_real_email(self):
        try:
            # Send a test email
            response = send_mail(
                subject="Test Email for Real Sending",
                message="This is a test email sent from the test case.",
                from_email="antrixphotosonam@gmail.com",
                recipient_list=["antrikshsaini96@gmail.com"],
            )

            # Assert the email was sent successfully
            self.assertEqual(response, 1)  # `send_mail` should return the number of emails sent
            print("Email sent successfully.")

        except smtplib.SMTPException as e:
            # If there's an SMTP issue, fail the test
            self.fail(f"SMTP error occurred: {e}")
        except Exception as e:
            # Catch any other exceptions and fail the test
            self.fail(f"Unexpected error occurred: {e}")

