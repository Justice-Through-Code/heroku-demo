from django.urls import path

from . import views

urlpatterns = [
    # todos/
    path('', views.todo, name='todo'),
    path('<int:task_id>', views.task, name='task')
]