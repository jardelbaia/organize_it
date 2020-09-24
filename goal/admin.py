from django.contrib import admin
from .models import Goal

class GoalAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)
admin.site.register(Goal, GoalAdmin)