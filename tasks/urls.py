from django.urls import path
from tasks import views

urlpatterns = [
    path('tasks/', views.list_tasks, name='list_tasks'),
]
