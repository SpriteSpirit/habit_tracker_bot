from django.core.management import call_command
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from habits.models import Habit
from habits.serializers import HabitSerializer
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

    def test_str_representation(self):
        """Проверяет, что метод __str__ возвращает корректную строку."""
        instance_str = f'{self.habit.action}: {self.habit.time} - {self.habit.place}'
        expected_str = f'habit1: 15:00:00 - test_place'
        self.assertEqual(str(instance_str), expected_str)

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


class HabitSerializerTestCase(APITestCase):
    """ Тестирование сериализатора привычки """

    def setUp(self) -> None:
        """ Создает экземпляр объекта для тестов """
        call_command('loaddata', 'test_data.json')

        self.user = User.objects.get(email='admin@localhost')
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

        self.habit = Habit.objects.get(pk=1)

    def test_serialize_habit(self):
        """ Проверяет, что сериализатор возвращает все поля """
        serializer = HabitSerializer(self.habit)
        print(serializer.data['pleasant_habit'])

        self.assertEqual(serializer.data['user'], 1)
        self.assertEqual(serializer.data['action'], 'habit1')
        self.assertEqual(serializer.data['place'], 'test_place')
        self.assertEqual(serializer.data['frequency'], 1)
        self.assertEqual(serializer.data['time'], '15:00:00')
        self.assertEqual(serializer.data['is_public'], True)
        self.assertEqual(serializer.data['pleasant_habit'], [
            {
                'user': 1,
                'action': 'habit2',
                'place': 'test',
                'frequency': 1,
                'execution_time': '00:02:00',
                'is_public': True,
                'linked_habit': 1
            }])

    def test_deserialize_habit(self):
        """ Проверяет, что десериализатор возвращает корректные данные """

        serializer = HabitSerializer(data=self.habit.__dict__)  # !!!
        self.assertTrue(serializer.is_valid())
        serializer.save()

        self.assertEqual(serializer.data['action'], 'habit1')
        self.assertEqual(serializer.data['is_public'], True)
        self.assertEqual(serializer.data['linked_habit'], None)

    def test_get_pleasant_habit(self):
        """ Проверяет, что сериализатор возвращает список приятных привычек """

        pleasant_habits = self.habit.linked_habits.all()
        serializer = HabitSerializer(pleasant_habits, many=True)

        self.assertEqual(serializer.data[0]['action'], 'habit2')
        self.assertEqual(serializer.data[0]['is_public'], True)
