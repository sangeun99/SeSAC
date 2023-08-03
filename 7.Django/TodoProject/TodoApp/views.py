from django.shortcuts import render, redirect
from .models import Task

# Create your views here.
def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'TodoApp/task_list.html', {'tasks': tasks})

def task_create(request):
    if request.method == 'POST' :
        new_title = request.POST['title']
        new_task = Task(title=new_title)
        new_task.save()
        return redirect('task_list')
    return render(request, 'TodoApp/task_create.html')

def task_detail(request, tid):
    task = Task.objects.filter(id=tid).first()
    return render(request, 'TodoApp/task_detail.html', {'tid': tid, 'task' : task})

def task_update(request, tid):
    task = Task.objects.filter(id=tid).first()
    if request.method == 'POST' :
        new_title = request.POST['title']
        Task.objects.filter(id=tid).update(title=new_title)
        return redirect('task_list')
    return render(request, 'TodoApp/task_update.html', {'tid': tid, 'task' : task})

def task_delete(request, tid):
    task = Task.objects.filter(id=tid)
    task.delete()
    return redirect('task_list')