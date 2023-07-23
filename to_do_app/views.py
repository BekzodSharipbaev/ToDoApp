from django.http import HttpRequest
from django.shortcuts import get_object_or_404, redirect, render

from .models import Task
from .forms import TaskForm

# Create your views here.


def home_page(request: HttpRequest):
    tasks = Task.objects.all()
    context = {"tasks": tasks}
    return render(request, 'to_do_app/home.html', context)


def show_task(request: HttpRequest, pk: int):
    task = get_object_or_404(Task, pk=pk)
    context = {'task': task}
    return render(request, 'to_do_app/task.html', context)


def add_task(request: HttpRequest):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TaskForm()
    context = {'form': form}
    return render(request, 'to_do_app/add_task.html', context)


def edit_task(request: HttpRequest, pk: int):
    task = get_object_or_404(Task, pk=pk)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TaskForm(instance=task)

    context = {'form': form}
    return render(request, 'to_do_app/add_task.html', context)


def delete_task(request: HttpRequest, pk: int):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('home')


def finish_task(request: HttpRequest, pk: int):
    task = get_object_or_404(Task, pk=pk)
    task.status = True
    task.save()
    return redirect('home')
