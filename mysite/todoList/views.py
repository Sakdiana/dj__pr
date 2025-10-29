from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .form import TaskForm


def task_list(request):
    status = request.GET.get('status')
    tasks = Task.objects.all().order_by('-created_at')

    if status == 'done':
        tasks = tasks.filter(completed=True)
    elif status == 'todo':
        tasks = tasks.filter(completed=False)

    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todoList')
    else:
        form = TaskForm()

    return render(request, 'todoList/index.html', {'tasks': tasks, 'form': form, 'status': status})


def task_edit(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('todoList')
    else:
        form = TaskForm(instance=task)
    return render(request, 'todoList/task_edit.html', {'form': form, 'task': task})


def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('todoList')
