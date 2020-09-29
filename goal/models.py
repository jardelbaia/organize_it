from django.db import models
from django.contrib.auth.models import User

class Goal(models.Model):
    title = models.CharField(max_length = 100)
    created = models.DateTimeField(auto_now_add =True)
    completed = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title

class SocialGoal(models.Model):
    title = models.CharField(max_length = 100)
    created = models.DateTimeField(auto_now_add= True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.title

