from django.contrib import admin
from .models import Goal, SocialGoal

class GoalAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)

class SocialAdmin(admin.ModelAdmin):
    pass
        
admin.site.register(Goal, GoalAdmin)
admin.site.register(SocialGoal, SocialAdmin)

