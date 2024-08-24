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
        if value < self.min_value or value > self.max_value:
            raise ValidationError(f'Периодичность должна быть от {self.min_value} до {self.max_value} дней')
