from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.reverse import reverse as api_reverse
from rest_framework.test import APITestCase

User = get_user_model()

class UserAPITestCase(APITestCase):

  def test_register_user_api_fail(self):
    url = api_reverse('api-auth:register')
    data = {
         'username': 'test@domain.com',
         'password': 'learncode',
    }
    response = self.client.post(url, data, format='json')
    self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    self.assertEqual(response.data['password2'][0], 'This field is required.')


  def test_register_user_api_success(self):
    url = api_reverse('api-auth:register')
    data = {
         'username': 'test@domain.com',
         'password': 'learncode',
         'password2': 'learncode'
    }
    response = self.client.post(url, data, format='json')
    self.assertEqual(response.status_code, status.HTTP_201_CREATE)
    token_exists = len(esponse.data.get("token", 0))
    self.assertGreater(token_len, 0)

  def test_login_user_api_success(self):
    url = api_reverse('api-auth:login')
    data = {
         'username': 'test@domain.com',
         'password': 'learncode',
    }
    response = self.client.post(url, data, format='json')
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    token_exists = len(esponse.data.get("token", 0))
    self.assertGreater(token_len, 0)


    




