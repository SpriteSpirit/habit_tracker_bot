from datetime import timedelta

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from users.models import User


NULLABLE = {'null': True, 'blank': True}


class Habit(models.Model):
    """ Привычка """
    objects = models.Manager()

    choices = [
        (1, 'Ежедневно'),
        (7, 'Еженедельно')
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='habits', verbose_name='Пользователь')
    action = models.CharField(max_length=100, verbose_name='Действие')
    place = models.CharField(max_length=50, verbose_name='Место')
    time = models.TimeField(verbose_name='Время')
    frequency = models.PositiveIntegerField(default=7, choices=choices,
                                            validators=[MinValueValidator(1), MaxValueValidator(7)],
                                            verbose_name='Периодичность')
    execution_time = models.DurationField(max_length=2, validators=[MaxValueValidator(timedelta(seconds=120))],
                                          verbose_name='Время на выполнение')
    is_pleasant = models.BooleanField(default=False, verbose_name='Приятная привычка')
    reward = models.CharField(max_length=100, **NULLABLE, verbose_name='Вознаграждение')
    linked_habit = models.ForeignKey('self', on_delete=models.SET_NULL, **NULLABLE, related_name='linked_habits',
                                     verbose_name='Связанная привычка', help_text='Только для приятных привычек')
    is_public = models.BooleanField(default=False, verbose_name='Публичная')

    class Meta:
        verbose_name = 'Привычка'
        verbose_name_plural = 'Привычки'

    def __str__(self):
        return f'{self.action}: {self.time} - {self.place}'
