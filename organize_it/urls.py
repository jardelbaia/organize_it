from django.contrib import admin
from django.urls import path
from main import views_main
from todo import views_todo
from goal import views_goal

urlpatterns = [
    path('admin/', admin.site.urls),

    #main
    path('',views_main.home, name='home'),
    path('logout/', views_main.logout_user, name='logout_user'),
    path('signup/', views_main.signup_user, name='signup_user'),
    path('apps/',views_main.apps, name='apps'),
    
    #todo
    path('current_todo/', views_todo.current_todo, name='current_todo'),
    path('completed_todo/', views_todo.completed_todo, name='completed_todo'),
    path('create_todo/', views_todo.create_todo, name='create_todo'),
    path('check_todo/<int:todo_pk>', views_todo.check_todo, name='check_todo'),
    path('check_completed_todo/<int:todo_pk>', views_todo.check_completed_todo, name='check_completed_todo'),
    path('check_todo/<int:todo_pk>/delete', views_todo.delete_todo, name='delete_todo'),
    path('check_todo/<int:todo_pk>/complete', views_todo.complete_todo, name='complete_todo'),
    path('check_todo/<int:todo_pk>/uncomplete', views_todo.uncomplete_todo, name='uncomplete_todo'),
   
    #goal
    path('current_goal/', views_goal.current_goal, name='current_goal'),
    path('completed_goal/', views_goal.completed_goal, name='completed_goal'),
    path('create_goal/', views_goal.create_goal, name='create_goal'),
    path('check_goal/<int:goal_pk>', views_goal.check_goal, name='check_goal'),
    path('check_completed_goal/<int:goal_pk>', views_goal.check_completed_goal, name='check_completed_goal'),
    path('check_goal/<int:goal_pk>/delete', views_goal.delete_goal, name='delete_goal'),
    path('check_goal/<int:goal_pk>/complete', views_goal.complete_goal, name='complete_goal'),
    path('check_goal/<int:goal_pk>/uncomplete', views_goal.uncomplete_goal, name='uncomplete_goal'),
    path('social_goal/', views_goal.social_goal, name='social_goal'),

]
