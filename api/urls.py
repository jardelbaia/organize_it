from django.urls import path
from . import views

urlpatterns = [

    # Todos
    path('todos/', views.TodoListCreate.as_view()),
    path('todos/completed', views.TodoCompletedList.as_view()),
    path('todos/<int:pk>', views.TodoRetrieveUpdateDestroy.as_view()),
    path('todos/<int:pk>/complete', views.TodoComplete.as_view()),
    path('todos/<int:pk>/uncomplete', views.TodoUncomplete.as_view()),

    # Goals
    path('goals/', views.GoalListCreate.as_view()),
    path('goals/completed', views.GoalCompletedList.as_view()),
    path('goals/<int:pk>', views.GoalRetrieveUpdateDestroy.as_view()),
    path('goals/<int:pk>/complete', views.GoalComplete.as_view()),
    path('goals/<int:pk>/uncomplete', views.GoalUncomplete.as_view()),

    # Auth
    path('signup', views.signup),
    path('login', views.login),

    
]