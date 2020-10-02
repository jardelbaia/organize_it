from django.shortcuts import render
from rest_framework import generics, permissions
from .serializers import TodoSerializer, GoalSerializer, TodoCompleteSerializer, GoalCompleteSerializer
from todo.models import Todo
from goal.models import Goal
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.parsers import JSONParser
from rest_framework.authtoken.models import Token

####################################################################
#                       Auth Views                                 #
####################################################################

@csrf_exempt
def signup(request):
    if request.method == 'POST':
        try:
            data = JSONParser().parse(request)
            user = User.objects.create_user(data['username'], password=data['password'])
            user.save()
            token = Token.objects.create(user=user)
            return JsonResponse({'token':str(token)}, status=201)
        except IntegrityError:
            return JsonResponse({'error':'Username has already been taken'}, status=400)
    
@csrf_exempt
def login(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        user = authenticate(request, username=data['username'], password=data['password'])
        if user is None:
            return JsonResponse({'error':'Could not login. Please check user and password.'}, status=400)
        else:
            try:
                token = Token.objects.get(user=user)
            except:
                token = Token.objects.create(user=user)
            return JsonResponse({'token':str(token)}, status=200)




####################################################################
#                   Todo App - API Views                           #
####################################################################
class TodoListCreate(generics.ListCreateAPIView):
    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Todo.objects.filter(user=user, completed=False)

    def perform_create(self,serializer):
        serializer.save(user=self.request.user)

class TodoCompletedList(generics.ListAPIView):
    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Todo.objects.filter(user=user, completed=True)

class TodoRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Todo.objects.filter(user=user)

class TodoComplete(generics.UpdateAPIView):
    serializer_class = TodoCompleteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Todo.objects.filter(user=user)

    def perform_update(self, serializer):
        serializer.instance.completed= True
        serializer.save()

class TodoUncomplete(generics.UpdateAPIView):
    serializer_class = TodoCompleteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Todo.objects.filter(user=user)

    def perform_update(self, serializer):
        serializer.instance.completed= False
        serializer.save()


####################################################################
#                   Goal App - API Views                           #
####################################################################
class GoalListCreate(generics.ListCreateAPIView):
    serializer_class = GoalSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Goal.objects.filter(user=user, completed=False)

    def perform_create(self,serializer):
        serializer.save(user=self.request.user)

class GoalCompletedList(generics.ListAPIView):
    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Goal.objects.filter(user=user, completed=True)

class GoalRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = GoalSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Goal.objects.filter(user=user,)

class GoalComplete(generics.UpdateAPIView):
    serializer_class = GoalCompleteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Goal.objects.filter(user=user)

    def perform_update(self, serializer):
        serializer.instance.completed= True
        serializer.save()

class GoalUncomplete(generics.UpdateAPIView):
    serializer_class = GoalCompleteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Goal.objects.filter(user=user)

    def perform_update(self, serializer):
        serializer.instance.completed= False
        serializer.save()