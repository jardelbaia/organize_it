from django.forms import ModelForm
from .models import Goal, SocialGoal

class GoalForm(ModelForm):
    class Meta:
        model = Goal
        fields = ['title']

class SocialForm(ModelForm):
    class Meta:
        model = SocialGoal
        fields = ['title']