from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import context, loader
from .models import Task
from .forms import *

# Create your views here.
def index(request):
    tasks = Task.objects.all()
    form = TaskForm()

    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/todo/')

    context = {
        'tasks': tasks,
        'form': form,
    }
    return render(request, 'todo/index.html', context)

def updateTask(request, pk):
    task = Task.objects.get(id = pk)
    form = TaskForm(instance = task)

    if request.method == "POST":
        form = TaskForm(request.POST, instance = task)
        if form.is_valid():
            form.save()
        return redirect('/todo/')

    context = {
        'task': task,
        'form': form,
    }
    
    return render(request, 'todo/updateTask.html', context)
    
def deleteTask(request, pk):
    task = Task.objects.get(id = pk)

    if request.method == "POST":
        task.delete()
        return redirect('/todo/')
    
    context = {
        'task': task,
    }

    return render(request, 'todo/deleteTask.html', context)