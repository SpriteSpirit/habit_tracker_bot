from rest_framework import generics

from users.models import User
from users.serializers import UserSerializer


# TODO: доступы permissions для просмотра и редактирования профиля пользователя
# TODO: доступы permissions для просмотра и редактирования профиля пользователя

class UserListAPIView(generics.ListAPIView):
    """ Список всех пользователей """

    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserRetrieveView(generics.RetrieveAPIView):
    """ Получение информации о конкретном пользователе """

    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserCreateAPIView(generics.CreateAPIView):
    """ Создание нового пользователя """

    serializer_class = UserSerializer


class UserUpdateAPIView(generics.UpdateAPIView):
    """ Редактирование информации о конкретном пользователе """

    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserDestroyAPIView(generics.DestroyAPIView):
    """ Удаление пользователя """

    serializer_class = UserSerializer
    queryset = User.objects.all()
