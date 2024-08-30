from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

from celery import shared_task
from django.utils import timezone

import requests

from config import settings
from habits.models import Habit
from habits.services import send_telegram_message


@shared_task
def send_telegram_reminders():
    url = settings.TELEGRAM_URL
    token = settings.TELEGRAM_TOKEN

    time_now = timezone.localtime()
    time = (time_now + relativedelta(minutes=1)).strftime('%H:%M')
    date_now = datetime.now().date().strftime('%Y-%m-%d')
    habits = Habit.objects.filter(time=time, is_pleasant=False, date_start=date_now)

    if habits:
        for habit in habits:
            print(habit)
            requests.post(
                url=f'{url}{token}/sendMessage',
                data={
                    'chat_id': habit.user.tg_chat_id,
                    'text': send_telegram_message(habit)
                }
            )
            habit.date_start += timedelta(days=habit.frequency)
            habit.save()
