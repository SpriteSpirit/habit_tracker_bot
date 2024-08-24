from django.core.management import call_command
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from users.models import User


class UserTestCase(APITestCase):
    """ Тестирование API для пользователя """

    def setUp(self) -> None:
        """ Создает экземпляры объектов для тестов """
        call_command('loaddata', 'test_data.json')
        self.user = User.objects.get(email='admin@localhost')

        self.client = APIClient()
        self.client.force_authenticate(user=self.user)


    def test_create_user(self):
        """ Тестирование создания пользователя """

        data = {
            'first_name': 'new_user',
            'last_name': 'new_user_last_name',
            'email': 'new_user@localhost',
            'password': 'new_user_password'
        }

        response = self.client.post('/users/create/', data=data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json()['email'], 'new_user@localhost')


    def test_get_user(self):
        """ Тестирование получения информации о пользователе """

        response = self.client.get(f'/users/view/{self.user.pk}/')
        print(response.json())

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['email'], 'admin@localhost')


    def test_update_user(self):
        """ Тестирование изменения информации о пользователе """

        data = {
            'first_name': 'updated_user',
            'last_name': 'updated_user_last_name',
            'email': 'updated_user@localhost',
            'password': 'updated_user_password'
        }

        response = self.client.put('/users/update/3/', data=data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['email'], 'updated_user@localhost')


    def test_delete_user(self):
        """ Тестирование удаления пользователя """

        response = self.client.delete('/users/delete/3/')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class TokenTestCase(APITestCase):
    """ Тестирование получения токена """
    def setUp(self) -> None:
        """ Создает экземпляр объекта для тестов """
        self.user = User.objects.create(email='admin@localhost')
        self.user.set_password('admin')
        self.user.save()
        print(self.user)

        self.client = APIClient()

    def test_get_token(self):
        """ Тестирование получения токена """

        data = {
            'email': self.user.email,
            'password': 'admin',
        }

        response = self.client.post('/users/token/', data=data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.json())


    def test_refresh_token(self):
        """ Тестирование получения нового токена на основе старого """

        # 1. Получить начальный токен
        data = {
            'email': self.user.email,
            'password': 'admin'
        }
        response = self.client.post('/users/token/', data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        refresh_token = response.json()['refresh']

        # 2. Отправить запрос на обновление
        data = {
            'refresh': refresh_token,
        }
        response = self.client.post('/users/token/refresh/', data=data)

        # 3. Проверить ответ
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.json())
