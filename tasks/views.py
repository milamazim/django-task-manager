from django.shortcuts import render, redirect
from tasks.models import Task
from tasks.forms import TaskForm

def task_list(request):
    tasks = Task.objects.order_by('-created_on')
    return render(request, 'list_task.html', {'tasks': tasks})

def new_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    
    return render(request, 'new_task.html', {'form': form})