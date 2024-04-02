from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render

# Create your views here.
from django.shortcuts import render, redirect

# views.py
from django.shortcuts import render, redirect

from Todo_app.forms import TaskForm
from .models import Task ,Group ,TaskList

def home(request):
    task_lists = TaskList.objects.filter(group__isnull=True)
    # Pass the filtered task lists to the template context
    tasks_Completed = Task.objects.filter(completed=True)
    tasks = Task.objects.filter(completed=False)
    tasks_importnat = Task.objects.filter(important=True)
    group = Group.objects.all()
    List=TaskList.objects.all()
    print(tasks_importnat)
    return render(request, 'Todo_app/index.html',
                  {'tasks': tasks ,
                   'Group':group,        
                   'task_lists': task_lists,
                   'List':List,
                  'tasks_Completed': tasks_Completed, 
                  'tasks_importnat': tasks_importnat })
    
def important_tasks(request):
    tasks_important = Task.objects.filter(important=True)
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            description = form.cleaned_data['description']
            important = form.cleaned_data['important']
            Task.objects.create(description=description, important=important)
            return redirect('important_tasks')
    return render(request, 'Todo_app/important.html', {'tasks_important': tasks_important, 'form': form})


def Planned_tasks(request):
    tasks_important = Task.objects.filter(important=True)
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            description = form.cleaned_data['description']
            important = form.cleaned_data['important']
            Task.objects.create(description=description, important=important)
            return redirect('Planned_tasks')
    return render(request, 'Todo_app/Planned.html', {'tasks_important': tasks_important, 'form': form})

def add_task2(request):
    if request.method == 'POST':
        description = request.POST.get('description')
        if description: 
            new_task = Task.objects.create(description=description)
            return redirect('home')  
    return render(request, 'Todo_app/add_task.html')


def task_list(request, task_list_id):
    tasks = Task.objects.filter(task_list_id=task_list_id,completed=False)
    tasks_compelte = Task.objects.filter(task_list_id=task_list_id,completed=True)
    context = {
        'tasks_compelte':tasks_compelte,
        'tasks': tasks,
        'task_list_id': task_list_id,  # Pass the task list ID to the template context
    }
    return render(request, 'Todo_app/task_list.html', context)

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
    
def create_group(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        Group.objects.create(name=name)
        return redirect('home')

def create_tasklist(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        group_id = request.POST.get('group')
        group = Group.objects.get(pk=group_id)  # Retrieve the Group object using its primary key
        TaskList.objects.create(name=name, group=group)
        return redirect('home')
    

from django.shortcuts import render, redirect
from .models import TaskList

def create_tasklistGroup(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        TaskList.objects.create(name=name)
        return redirect('home')  # Assuming 'home' is the name of your home view


def add_task(request, task_list_id):
    task_list = get_object_or_404(TaskList, id=task_list_id)
    if request.method == 'POST':
        description = request.POST.get('description')
        Task.objects.create(description=description, task_list=task_list)
        return redirect('task_list', task_list_id=task_list_id)  

    
from django.shortcuts import get_object_or_404, redirect
from .models import Group



def edit_group(request, group_id):
    if request.method == 'POST':
        group = get_object_or_404(Group, id=group_id)
        new_name = request.POST.get('name')
        if new_name:
            group.name = new_name
            group.save()
            return redirect('home') 
        

def delete_group(request, group_id):
    if request.method == 'POST':
        group = get_object_or_404(Group, id=group_id)
        group.delete()
        return redirect('home')

    

def edit_tasklist(request, tasklist_id):
    task_list = get_object_or_404(TaskList, id=tasklist_id)
    if request.method == 'POST':
        new_name = request.POST.get('name')
        if new_name:
            task_list.name = new_name
            task_list.save()
    return redirect('home')  # Redirect to the homepage or any other page

def delete_tasklist(request, tasklist_id):
    task_list = get_object_or_404(TaskList, id=tasklist_id)
    if request.method == 'POST':
        task_list.delete()
    return redirect('home')  



def create_task(request, task_list_id):
    task_list = TaskList.objects.get(id=task_list_id)
    if request.method == 'POST':
        description = request.POST.get('description')
        Task.objects.create(task_list=task_list, description=description)
        return redirect('home')  

def mark_as_incomplete(request, task_id):
    task = Task.objects.get(id=task_id)
    task.completed = False
    task.save()
    return redirect('home')


def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':

        task.description = request.POST['description']
        task.save()
        return redirect('home')  

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
 
        task.delete()
        return redirect('home') 
    


# def edit_task(request, task_id):
#     task = get_object_or_404(Task, id=task_id)
#     if request.method == 'POST':
#         description = request.POST.get('description')
#         completed = request.POST.get('completed')  # Assuming you have a checkbox or similar for completion status
#         if description is not None:
#             task.description = description
#             task.completed = completed
#             task.save()
#     return redirect('home')  # Redirect to the homepage or any other page

# def delete_task(request, task_id):
    # task = get_object_or_404(Task, id=task_id)
    # if request.method == 'POST':
    #     task.delete()
    # return redirect('home') 
# def edit_task(request, group_id, list_id, task_id):
#     task = Task.objects.get(id=task_id)
#     if request.method == 'POST':
#         task.description = request.POST.get('description')
#         task.completed = request.POST.get('completed', False)
#         task.save()
#         return redirect('home')  # Redirect to appropriate page
#     return render(request, 'edit_task.html', {'task': task})

# def delete_task(request, group_id, list_id, task_id):
#     task = Task.objects.get(id=task_id)
#     if request.method == 'POST':
#         task.delete()
#         return redirect('home')  # Redirect to appropriate page
