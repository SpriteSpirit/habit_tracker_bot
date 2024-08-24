from rest_framework import serializers
from.models import Habit
from .validators import PleasantHabit


class PleasantHabitSerializer(serializers.ModelSerializer):
    """ Сериализатор приятной привычки """
    class Meta:
        model = Habit
        fields = ('user', 'action', 'place', 'frequency', 'execution_time', 'is_public', 'linked_habit',)


class UserHabitSerializer(serializers.ModelSerializer):
    """ Сериализатор привычки """
    pleasant_habit = serializers.SerializerMethodField()

    class Meta:
        model = Habit
        fields = '__all__'

    def get_pleasant_habit(self, obj):
        # Получить список приятных привычек для текущей привычки
        pleasant_habits = obj.linked_habits.all()
        serializer = PleasantHabitSerializer(pleasant_habits, many=True)
        return serializer.data

class HabitCreateSerializer(serializers.ModelSerializer):
    """ Сериализатор создания привычки """
    class Meta:
        model = Habit
        fields = '__all__'
        validators = [
            PleasantHabit(fields)
        ]
