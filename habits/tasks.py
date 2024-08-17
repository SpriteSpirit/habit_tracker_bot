from datetime import timezone, datetime
from dateutil.relativedelta import relativedelta

from celery import shared_task
import telebot
from django.contrib.sites import requests

from habits.models import Habit

API_TOKEN = '7367321933:AAFGQqo63iYZqTj7liHqLH6SLxPmIL8ig_w'

bot = telebot.TeleBot(API_TOKEN)


@shared_task
def send_telegram_reminders():
    url = 'https://api.telegram.org/bot'
    token = API_TOKEN

    time_now = timezone.localtime()
    time = (time_now + relativedelta(minutes=5)).strftime('%H:%M')
    date_now = datetime.now().date().strftime('%Y-%m-%d')
    habits = Habit.objects.filter(time=time, pleasant_habit=False, date_start=date_now)

    if habits:
        for habit in habits:
            requests.post(
                url=f'{url}{token}/sendMessage',
                data={
                    'chat_id': habit.user.telegram_id,
                    'text': create_telegram_message(habit)
                }
            )
            habit.date_start += timedelta(days=habit.period)
            habit.save()