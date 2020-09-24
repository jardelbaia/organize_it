from django.shortcuts import render, redirect, get_object_or_404
from .forms import TodoForm
from .models import Todo
from django.contrib.auth.decorators import login_required

@login_required
def current_todo(request):
    todos = Todo.objects.filter(user=request.user, completed = False)\
    .order_by('-created')
    return render(request,'todo/current_todo.html', {'todos':todos})

@login_required
def completed_todo(request):

    todos = Todo.objects.filter(user=request.user, completed = True)\
    .order_by('-created')
    return render(request,'todo/completed_todo.html', {'todos':todos})

@login_required
def create_todo(request):
    if request.method=='GET':
        return render(request, 'todo/create_todo.html',{'form': TodoForm()})
    else:
        try:
            form = TodoForm(request.POST)
            newtodo = form.save(commit=False)    
            newtodo.user = request.user
            newtodo.save()
            return redirect('current_todo')
        except ValueError:
            return render(request, 'todo/create_todo.html',\
            {'form': TodoForm(),'error':'Something went wrong. Please try again.'})

@login_required
def check_todo(request, todo_pk):
    todo = get_object_or_404(Todo, pk=todo_pk, user=request.user)
    if request.method=='GET':
        form = TodoForm(instance=todo)
        return render(request, 'todo/check_todo.html', {'form':form,'todo':todo})
    else:
        try:
            form = TodoForm(request.POST, instance=todo)
            form.save()
            return redirect('current_todo')
        except ValueError:
            return render(request,'todo/check_todo.html', {'todo':todo, 'form':form,\
            'error':'Something went wrong. Please try again'})

@login_required
def check_completed_todo(request,todo_pk):
    todo = get_object_or_404(Todo, pk=todo_pk, user=request.user)
    if request.method=='GET':
        form = TodoForm(instance=todo)
        return render(request, 'todo/check_completed_todo.html', {'form':form,'todo':todo})
    else:
        try:
            form = TodoForm(request.POST, instance=todo)
            form.save()
            return redirect('completed_todo')
        except ValueError:
            return render(request,'todo/check_completed_todo.html', {'todo':todo, 'form':form,\
            'error':'Something went wrong. Please try again'})

@login_required        
def delete_todo(request,todo_pk):
    todo = get_object_or_404(Todo, pk=todo_pk, user=request.user)
    if request.method=='POST':
        todo.delete()
        return redirect('current_todo')

@login_required
def complete_todo(request,todo_pk):
    todo = get_object_or_404(Todo, pk=todo_pk, user=request.user)
    if request.method=='POST':
        todo.completed = True
        todo.save()
        return redirect('current_todo')

@login_required
def uncomplete_todo(request,todo_pk):
    todo = get_object_or_404(Todo, pk=todo_pk, user=request.user)
    if request.method=='POST':
        todo.completed = False
        todo.save()
        return redirect('current_todo')