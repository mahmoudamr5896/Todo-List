from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect

# views.py
from django.shortcuts import render, redirect
from .models import Task ,Group ,TaskList

def home(request):
    tasks_Completed = Task.objects.filter(completed=True)
    tasks = Task.objects.filter(completed=False)
    tasks_importnat = Task.objects.filter(important=True)
    group = Group.objects.all()
    List=TaskList.objects.all()
    print(tasks_importnat)
    return render(request, 'Todo_app/index.html',
                  {'tasks': tasks ,
                   'Group':group,
                   'List':List,
                  'tasks_Completed': tasks_Completed, 
                  'tasks_importnat': tasks_importnat })
    



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


def mark_task_as_completed(request, task_id):
    task = Task.objects.get(id=task_id)
    task.completed = True
    task.save()
    return JsonResponse({'message': 'Task marked as completed successfully'})

def mark_task_as_important(request, task_id):
        task = Task.objects.get(id=task_id)
        task.important = not task.important # Toggle importance
        print(task)
        task.save()
        return JsonResponse({'message': 'Task marked as important successfully'})
    