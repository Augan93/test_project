from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from . models import Car
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User


class CarTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_superuser()

    def test_create_car(self):
        user = User.objects.get(pk=1)
        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + access_token)
        url = reverse('cars:car-create-list')
        data = {'color': 'red', 'year': 2018, 'manufacturer': 'Lexus'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

