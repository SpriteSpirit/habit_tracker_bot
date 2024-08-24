from rest_framework import serializers
from.models import Habit

class UserHabitSerializer(serializers.ModelSerializer):
    """ Сериализатор привычки """
    class Meta:
        model = Habit
        fields = '__all__'
