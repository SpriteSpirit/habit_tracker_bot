from datetime import datetime, timedelta

from dateutil.relativedelta import relativedelta
from django.utils import timezone
from rest_framework.serializers import ValidationError


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
        is_pleasant = dict(value).get('is_pleasant')
        linked_habit = dict(value).get('linked_habit')
        reward = dict(value).get('reward')

        if is_pleasant and reward:
            raise ValidationError('Приятная привычка не может иметь награду')

        if linked_habit and not is_pleasant:
            raise ValidationError('Связанная привычка должна быть приятной')

        # Проверка на одновременное заполнение полей вознаграждения и связанной привычки
        if reward and linked_habit:
            raise ValidationError('Нельзя заполнить одновременно и поле вознаграждения, и поле связанной привычки')


class FrequencyValidator:
    """
    Проверяет, что привычка выполняется не реже одного раза в 7 дней и не чаще одного раза в день.
    """
    def __init__(self, min_value=1, max_value=7):
        self.min_value = min_value
        self.max_value = max_value

    def __call__(self, value):
        frequency = dict(value).get('frequency')

        if int(frequency) < self.min_value or int(frequency) > self.max_value:
            raise ValidationError(f'Периодичность должна быть от {self.min_value} до {self.max_value} дней. '
                                  f'Нельзя выполнять привычку реже, чем 1 раз в 7 дней.')


class TimeValidator:
    """
    Проверяет, что время назначено не ранее чем за 5 минут до выполнения
    """

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        start_time = value.get('time')
        start_date = value.get('date_start')

        date_now = datetime.now().date()
        current_time = timezone.localtime()

        if start_date == date_now:
            start_datetime = datetime.combine(date_now, start_time)
            five_minutes_ago = start_datetime - relativedelta(minutes=5)

            print(start_datetime.time(), five_minutes_ago.time())  # Вывод для отладки
            if current_time.time() >= five_minutes_ago.time():
                print(start_datetime.time() > five_minutes_ago.time())
                raise ValidationError(
                    f'Задача "{value.get("action")}" может быть назначена не ранее чем за 5 минут до выполнения.')
