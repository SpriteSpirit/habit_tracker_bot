from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from habits.models import Habit
from habits.permissions import IsOwnerOrReadOnly
from habits.serializers import HabitSerializer, HabitCreateSerializer


class HabitViewSet(viewsets.ModelViewSet):
    """ Контроллер для управления привычками """
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def get_serializer(self, *args, **kwargs):
        if self.action in ['create', 'update']:
            return HabitCreateSerializer(*args, **kwargs)
        elif self.action in ['list', 'retrieve']:
            return HabitSerializer(*args, **kwargs)
        return super().get_serializer(*args, **kwargs)

    def perform_create(self, serializer):
        """ Сохраняет привычку пользователя """
        serializer.save(user=self.request.user)

    def get_queryset(self):
        """ Получает привычки, отфильтрованные по параметру запроса is_public """
        if self.request.query_params.get('is_public'):
            return Habit.objects.filter(is_public=True)
        return super().get_queryset()
