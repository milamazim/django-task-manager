from django.shortcuts import render, redirect
from tasks.models import Task, Status
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

def task_edit(request, pk):
    task = Task.objects.get(id=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'edit_task.html', {'form': form, 'task': task})


def task_delete(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return redirect('task_list')
