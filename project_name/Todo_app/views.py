from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.template.loader import render_to_string
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

def unmark_completed(request, task_id):
    try:
        task = Task.objects.get(id=task_id)
        task.completed = False
        task.save()
        return JsonResponse({'success': True})
    except Task.DoesNotExist:
        return JsonResponse({'success': False, 'error': 'Task not found'})


def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'Todo_app/task_list.html', {'tasks': tasks})

def mark_task_as_completed(request, task_id):
    try:
        task = Task.objects.get(id=task_id)
        task.completed = True
        task.save()
        
        # Retrieve all completed tasks
        tasks_completed = Task.objects.filter(completed=True)
        
        # Render the HTML template for the completed tasks
        html_content = render_to_string('completed_tasks.html', {'tasks_completed': tasks_completed})
        
        return JsonResponse({'success': True, 'html_content': html_content})
    except Task.DoesNotExist:
        return JsonResponse({'success': False, 'error': 'Task not found'})

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
    

# def add_task(request, task_list_id):
#     if request.method == 'POST':
#         description = request.POST.get('description')
#         Task.objects.create(description=description, task_list_id=task_list_id)
#         return redirect('home')  # Redirect to the homepage or any other page
#     else:
#         # Handle GET request if needed
#         pass

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
    return redirect('home')  # Redirect to the homepage or any other page


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
def edit_task(request, group_id, list_id, task_id):
    task = Task.objects.get(id=task_id)
    if request.method == 'POST':
        task.description = request.POST.get('description')
        task.completed = request.POST.get('completed', False)
        task.save()
        return redirect('home')  # Redirect to appropriate page
    return render(request, 'edit_task.html', {'task': task})

def delete_task(request, group_id, list_id, task_id):
    task = Task.objects.get(id=task_id)
    if request.method == 'POST':
        task.delete()
        return redirect('home')  # Redirect to appropriate page
    return render(request, 'delete_task.html', {'task': task})

def create_task(request, task_list_id):
    task_list = TaskList.objects.get(id=task_list_id)
    if request.method == 'POST':
        description = request.POST.get('description')
        Task.objects.create(task_list=task_list, description=description)
        return redirect('home')  
