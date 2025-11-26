from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo
from django.contrib import messages

def home(request):
    todos = Todo.objects.all()
    return render(request, 'home.html', {'todos': todos})

def create_todo(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description', '')
        due_date = request.POST.get('due_date') or None
        
        if title:
            Todo.objects.create(
                title=title,
                description=description,
                due_date=due_date
            )
            messages.success(request, 'TODO created successfully!')
        return redirect('home')
    return redirect('home')

def edit_todo(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)
    
    if request.method == 'POST':
        todo.title = request.POST.get('title')
        todo.description = request.POST.get('description', '')
        todo.due_date = request.POST.get('due_date') or None
        todo.save()
        messages.success(request, 'TODO updated successfully!')
        return redirect('home')
    
    return render(request, 'edit_todo.html', {'todo': todo})

def delete_todo(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)
    todo.delete()
    messages.success(request, 'TODO deleted successfully!')
    return redirect('home')

def toggle_resolved(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)
    todo.resolved = not todo.resolved
    todo.save()
    return redirect('home')