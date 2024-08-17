from django.shortcuts import render


class HabitViewSet(ModelViewSet):
    """  """
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
