from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect


def home(request):
    tasks = Task.objects.all()
    print(tasks)
    return render(request, 'Todo_app/index.html',{'tasks': tasks})
    

# views.py
from django.shortcuts import render, redirect
from .models import Task

def add_task(request):
    if request.method == 'POST':
        description = request.POST.get('description')
        if description: 
            new_task = Task.objects.create(description=description)
            return redirect('home')  
    return render(request, 'Todo_app/add_task.html')


def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'Todo_app/task_list.html', {'tasks': tasks})
