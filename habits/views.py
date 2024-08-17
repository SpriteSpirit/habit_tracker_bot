from rest_framework import viewsets, pagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from habits.models import Habit
from habits.permissions import IsOwnerOrReadOnly
from habits.serializers import HabitSerializer


class HabitViewSet(viewsets.ModelViewSet):
    """ Контроллер для управления привычками """
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer

    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    pagination_class = pagination.PageNumberPagination

    def perform_create(self, serializer):
        """ Сохраняет привычку пользователя """
        serializer.save(user=self.request.user)

    def get_queryset(self):
        """ Получает привычки, отфильтрованные по параметру запроса `is_public` """
        if self.request.query_params.get('is_public'):
            return Habit.objects.filter(is_public=True)
        return super().get_queryset()
