from django.contrib import admin

from habits.models import Habit


@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    list_display = ('action', 'time', 'place', 'frequency', 'execution_time',
                    'is_pleasant', 'reward', 'linked_habit', 'is_public')
    search_fields = ('action', 'time', 'place', 'reward')
    list_filter = ('is_pleasant', 'linked_habit', 'is_public')
