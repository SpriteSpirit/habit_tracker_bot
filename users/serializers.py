from rest_framework import serializers

from habits.models import Habit
from users.models import User


class HabitSerializer(serializers.Serializer):
    """ Сериализатор привычки """
    class Meta:
        model = Habit
        fields = '__all__'


class UserSerializer(serializers.Serializer):
    """ Сериализатор пользователя """
    habits = HabitSerializer(source='habit', many=True, read_only=True)

    class Meta:
        model = User
        fields = '__all__'