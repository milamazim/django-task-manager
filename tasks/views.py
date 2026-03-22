from django.shortcuts import render
from tasks.models import Task, Status

def list_tasks(request):
    list_tasks = Task.objects.all()
    return render(request, 'list_task.html', {'status': list_tasks})
