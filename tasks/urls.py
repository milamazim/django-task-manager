from django.urls import path
from tasks import views

urlpatterns = [
    path('tasks/', views.task_list, name='task_list'),
    path('tasks/new/', views.new_task, name='new_task'),
]
