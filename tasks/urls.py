from django.urls import path
from tasks import views

urlpatterns = [
    path('tasks/', views.list_tasks, name='list_tasks'),
    path('new_task/', views.new_task, name='new_task'),
]
