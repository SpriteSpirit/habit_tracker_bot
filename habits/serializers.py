from rest_framework import serializers
from .models import Habit
from .validators import PleasantHabit, FrequencyValidator


class PleasantHabitSerializer(serializers.ModelSerializer):
    """ Сериализатор приятной привычки """
    class Meta:
        model = Habit
        fields = ('user', 'action', 'place', 'frequency', 'execution_time', 'is_public', 'linked_habit',)


class HabitSerializer(serializers.ModelSerializer):
    """ Сериализатор привычки """
    pleasant_habit = serializers.SerializerMethodField()

    class Meta:
        model = Habit
        fields = '__all__'
        validators = [
            FrequencyValidator()
        ]

    def get_pleasant_habit(self, instance):
        # Получить список приятных привычек для текущей привычки
        pleasant_habits = instance.linked_habits.all()
        serializer = PleasantHabitSerializer(pleasant_habits, many=True)
        return serializer.data


class HabitCreateSerializer(serializers.ModelSerializer):
    """ Сериализатор создания привычки """
    class Meta:
        model = Habit
        fields = '__all__'
        validators = [
            PleasantHabit(fields),
            FrequencyValidator()
        ]
