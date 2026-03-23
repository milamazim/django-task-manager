from django.urls import path
from tasks import views

urlpatterns = [
    path('tasks/', views.task_list, name='task_list'),
    path('tasks/new/', views.new_task, name='new_task'),
    path('tasks/<int:pk>/update/', views.task_finish, name='task_finish'),
    path('tasks/<int:pk>/delete/', views.task_delete, name='task_delete'),
]
