from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Todo
from .forms import TodoForm

# Create your views here.
def todo(request):
    if request.method == 'GET':
        tasks = Todo.objects.all().order_by('-task_id')
        form = TodoForm()
        return render(request, 'list.html', context={'form': form, 'tasks': tasks })
        
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data['task']
            Todo.objects.create(task=task)
        return HttpResponseRedirect(reverse('todo'))
        
def task(request, task_id):
    if request.method == 'GET':
        task = Todo.objects.get(pk=task_id)
        form = TodoForm(initial={'task': task.task })
        form.fields['task'].label = "Edit task"
        return render(request, 'detail.html', { 'form': form, 'task_id': task_id })
    if request.method == 'POST':
        if 'save' in request.POST:
            form = TodoForm(request.POST)
            if form.is_valid():
                task = form.cleaned_data['task']
                Todo.objects.filter(pk=task_id).update(task=task)
        elif 'delete' in request.POST:
             Todo.objects.filter(pk=task_id).delete()
        return HttpResponseRedirect(reverse('todo'))