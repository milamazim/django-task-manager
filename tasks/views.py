from django.shortcuts import render, redirect
from tasks.models import Task
from tasks.forms import TaskForm

def list_tasks(request):
    lists = Task.objects.all()
    return render(request, 'list_task.html', {'tasks': lists})

def new_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lists')
    else:
        form = TaskForm()
    
    return render(request, 'new_task.html', {'form': form})