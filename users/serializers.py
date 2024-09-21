from rest_framework import serializers

from habits.models import Habit
from users.models import User


class HabitSerializer(serializers.ModelSerializer):
    """ Сериализатор привычки """

    class Meta:
        model = Habit
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    """ Сериализатор пользователя """

    habits = HabitSerializer(source='habit', many=True, read_only=True)

    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')

        user = User.objects.create(
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            tg_chat_id=validated_data['tg_chat_id'],
        )

        user.set_password(password)
        user.save()
        return user

    def update(self, instance, validated_data):
        """ Обновление информации о пользователе """

        instance.email = validated_data.get('email', instance.email)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.tg_chat_id = validated_data.get('tg_chat_id', instance.tg_chat_id)

        if 'password' in validated_data:
            instance.set_password(validated_data['password'])

        instance.save()
        return instance
