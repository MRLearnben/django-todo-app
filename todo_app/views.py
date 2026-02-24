from django.shortcuts import render, redirect, get_object_or_404
from .models import ToDo
from django.contrib import messages  # For success messages

def todo_list(request):  # List all todos
    todos = ToDo.objects.all()  # Get all from database
    return render(request, 'todo_list.html', {'todos': todos})

def add_todo(request):  # Add new
    if request.method == 'POST':  # If form submitted
        title = request.POST['title']
        description = request.POST.get('description', '')
        ToDo.objects.create(title=title, description=description)
        messages.success(request, 'Todo added successfully!')
        return redirect('todo_list')
    return render(request, 'add_todo.html')

def update_todo(request, pk):  # Update existing
    todo = get_object_or_404(ToDo, pk=pk)
    if request.method == 'POST':
        todo.title = request.POST['title']
        todo.description = request.POST.get('description', '')
        todo.save()
        messages.success(request, 'Todo updated successfully!')
        return redirect('todo_list')
    return render(request, 'update_todo.html', {'todo': todo})

def delete_todo(request, pk):  # Delete
    todo = get_object_or_404(ToDo, pk=pk)
    todo.delete()
    messages.success(request, 'Todo deleted successfully!')
    return redirect('todo_list')

def toggle_completed(request, pk):  # Toggle status (optional)
    todo = get_object_or_404(ToDo, pk=pk)
    todo.completed = not todo.completed
    todo.save()
    messages.success(request, 'Todo status toggled!')
    return redirect('todo_list')