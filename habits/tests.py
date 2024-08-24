from django.core.management import call_command
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from habits.models import Habit
from users.models import User


class HabitTestCase(APITestCase):
    """ Тестирование привычек """

    def setUp(self) -> None:
        call_command('loaddata', 'test_data.json')
        self.user = User.objects.get(email='admin@localhost')
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

        self.habit = Habit.objects.get(pk=1)

    def test_create_habit(self):
        """ Тестирование создания привычки """

        data = {
            'user': 1,
            'action': 'Test action',
            'place': 'Test place',
            'time': '12:00',
            'frequency': 1,
            'execution_time': '01:00',
            'is_pleasant': True,
            'reward': None,
            'linked_habit': None,
            'is_public': False
        }

        response = self.client.post('', data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json()['action'], 'Test action')


    def test_list_habits(self):
        """ Тестирование получения списка привычек """

        response = self.client.get('', format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['count'], 3)


    def test_get_habit(self):
        """ Тестирование получения информации о привычке """

        response = self.client.get(f'/{self.habit.pk}/', format='json')
        print(response.json())

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['action'], 'habit1')


    def test_update_habit(self):
        """ Тестирование изменения информации о привычке """

        data = {
            'action': 'habit1 updated',
            'place': 'Test place updated',
            'time': '13:00',
            'frequency': 1,
            'execution_time': '02:00',
            'is_pleasant': True,
            'reward': None,
            'linked_habit': 2,
            'is_public': True
        }

        response = self.client.put(f'/{self.habit.pk}/', data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['action'], 'habit1 updated')


    def test_delete_habit(self):
        """ Тестирование удаления привычки """

        response = self.client.delete(f'/{self.habit.pk}/', format='json')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
