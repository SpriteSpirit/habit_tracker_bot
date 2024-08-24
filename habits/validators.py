from _pydatetime import timedelta

from rest_framework.validators import ValidationError


class PleasantHabit:
    """
    Проверка приятной привычки, связанной привычки и вознаграждения.

    В модели не должно быть заполнено одновременно и поле вознаграждения, и поле связанной привычки.
    Можно заполнить только одно из двух полей.

    В связанные привычки могут попадать только привычки с признаком приятной привычки.
    """
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        """ Проверка, что привычка является приятной и не содержит связанной привычки и вознаграждения """
        pleasant_habit = dict(value).get('is_pleasant')
        linked_habit = dict(value).get('linked_habit')
        reward = dict(value).get('reward')

        if pleasant_habit and reward:
            raise ValidationError('Приятная привычка не может иметь награду')

        if linked_habit and not pleasant_habit:
            raise ValidationError('Связанная привычка должна быть приятной')

        # Проверка на одновременное заполнение полей вознаграждения и связанной привычки
        if reward and linked_habit:
            raise ValidationError('Нельзя заполнить одновременно и поле вознаграждения, и поле связанной привычки')
