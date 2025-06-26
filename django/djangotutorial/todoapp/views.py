from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import Todo
from .forms import TodoForm

class CustomLoginView(LoginView):
    template_name = 'todoapp/login.html'
    
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful!')
            return redirect('todo_list')
    else:
        form = UserCreationForm()
    return render(request, 'todoapp/register.html', {'form': form})

@login_required
def todo_list(request):
    todos = Todo.objects.filter(user=request.user)
    
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = request.user
            todo.save()
            messages.success(request, 'Todo added successfully!')
            return redirect('todo_list')
    else:
        form = TodoForm()
    
    return render(request, 'todoapp/todo_list.html', {
        'todos': todos,
        'form': form
    })

@login_required
def toggle_todo(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id, user=request.user)
    todo.completed = not todo.completed
    todo.save()
    return redirect('todo_list')

@login_required
def delete_todo(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id, user=request.user)
    todo.delete()
    messages.success(request, 'Todo deleted successfully!')
    return redirect('todo_list')