from django.shortcuts import render, redirect, get_object_or_404
from .forms import GoalForm
from .models import Goal, SocialGoal
from django.contrib.auth.decorators import login_required

@login_required
def current_goal(request):
    goals = Goal.objects.filter(user=request.user, completed = False)\
    .order_by('-created')
    return render(request,'goal/current_goal.html', {'goals':goals}) 

@login_required
def completed_goal(request):
    goals = Goal.objects.filter(user=request.user, completed = True)\
    .order_by('-created')
    return render(request,'goal/completed_goal.html', {'goals':goals})

@login_required
def create_goal(request):
    if request.method== 'GET':
        return render(request,'goal/create_goal.html', {'form': GoalForm()})
    else:
        try:
            form = GoalForm(request.POST)
            newgoal = form.save(commit=False)    
            newgoal.user = request.user
            newgoal.save()
            return redirect('current_goal')
        except ValueError:
            return render(request, 'goal/create_goal.html',\
            {'form': GoalForm(),'error':'Something went wrong. Please try again.'})
    
@login_required    
def check_goal(request, goal_pk):
    goal = get_object_or_404(Goal, pk=goal_pk, user=request.user)
    if request.method=='GET':
        form = GoalForm(instance=goal)
        return render(request, 'goal/check_goal.html', {'form':form,'goal':goal})
    else:
        try:
            form = GoalForm(request.POST, instance=goal)
            form.save()
            return redirect('current_goal')
        except ValueError:
            return render(request,'goal/check_goal.html', {'goal':goal, 'form':form,\
            'error':'Something went wrong. Please try again'})

@login_required
def check_completed_goal(request, goal_pk):
    goal = get_object_or_404(Goal, pk=goal_pk, user=request.user)
    if request.method=='GET':
        form = GoalForm(instance=goal)
        return render(request, 'goal/check_completed_goal.html', {'form':form,'goal':goal})
    else:
        try:
            form = GoalForm(request.POST, instance=goal)
            form.save()
            return redirect('completed_goal')
        except ValueError:
            return render(request,'goal/check_completed_goal.html', {'goal':goal, 'form':form,\
            'error':'Something went wrong. Please try again'})

@login_required
def delete_goal(request, goal_pk):
    goal = get_object_or_404(Goal, pk=goal_pk, user=request.user)
    if request.method=='POST':
        goal.delete()
        return redirect('current_goal')
    
@login_required    
def complete_goal(request,goal_pk):
    goal = get_object_or_404(Goal, pk=goal_pk, user=request.user)
    if request.method=='POST':
        goal.completed = True
        goal.save()

        form = SocialGoal()
        form.title = goal.title
        form.user = goal.user
        form.save()
        return redirect('social_goal')

@login_required
def uncomplete_goal(request,goal_pk):
    goal = get_object_or_404(Goal, pk=goal_pk, user=request.user)

    if request.method=='POST':
        goal.completed = False
        goal.save()
        
        return redirect('current_goal')

@login_required
def social_goal(request):   
    socials =  SocialGoal.objects.all().order_by('-created')
    return render(request,'goal/social_goal.html',{'socials': socials})