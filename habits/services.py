def send_telegram_message(habit):
    """ Создание привычки """
    message = ''

    if not habit.is_pleasant:
        message = f'Напоминание: {habit.action} в {habit.time} в {habit.place}. '
        if habit.linked_habit:
            message += (f'Приятная привычка за выполнение: {habit.linked_habit.action} в {habit.linked_habit.time} '
                        f'в {habit.linked_habit.place}')
        elif habit.reward:
            message += f'Вознаграждение за выполнение: {habit.reward}'

    return message
