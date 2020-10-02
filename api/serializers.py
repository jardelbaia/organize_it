from rest_framework import serializers
from todo.models import Todo
from goal.models import Goal

class TodoSerializer(serializers.ModelSerializer):
    created = serializers.ReadOnlyField()
    completed = serializers.ReadOnlyField()

    class Meta:
        model = Todo
        fields = ['id','title','desc','created','important','completed']
   
class TodoCompleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['id']
        read_only_fields = ['title','desc','created','important','completed']
             
class GoalSerializer(serializers.ModelSerializer):
    created = serializers.ReadOnlyField()
    completed = serializers.ReadOnlyField()

    class Meta:
        model = Goal
        fields = ['id','title','created','completed']
        
 
class GoalCompleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['id']
        read_only_fields = ['title','created','completed']
             
    