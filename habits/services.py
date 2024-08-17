def create_telegram_message(habit):
    """ Создание привычки """
    message = ''

    if not habit.pleasant_habit:
        message = f'Напоминание: {habit.action} в {habit.time} в {habit.place}. '
        if habit.related_habit:
            message += (f'Приятная привычка за выполнение: {habit.related_habit.action} в {habit.related_habit.time} '
                        f'в {habit.related_habit.place}')
        elif habit.reward:
            message += f'Вознаграждение за выполнение: {habit.reward}'

    return message
