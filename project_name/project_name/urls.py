"""
URL configuration for project_name project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from asyncio import create_task
from django.contrib import admin
from django.urls import path

from Todo_app.views import create_tasklist, delete_group, delete_task, delete_tasklist, edit_group, edit_task, edit_tasklist, home , add_task2, mark_as_incomplete ,task_list ,mark_task_as_completed,mark_task_as_important,create_group,add_task
from Todo_app import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name='home'), 
    path('add_task2/', add_task2, name='add_task2'),
    path('task_list/', task_list, name='task_list'),
    path('important/', views.important_tasks, name='important_tasks'),
    path('mark_completed/<int:task_id>/', mark_task_as_completed, name='mark_completed'),
    path('mark_important/<int:task_id>/', mark_task_as_important, name='mark_importan'),
    path('create-group/', create_group, name='create_group'),
    path('create-tasklist/', create_tasklist, name='create_tasklist'),
    path('add_task/<int:task_list_id>/', add_task, name='add_task'),
    path('edit-group/<int:group_id>/', edit_group, name='edit_group'),
    path('delete-group/<int:group_id>/', delete_group, name='delete_group'),
    path('edit-tasklist/<int:tasklist_id>/', edit_tasklist, name='edit_tasklist'),
    path('delete-tasklist/<int:tasklist_id>/', delete_tasklist, name='delete_tasklist'),
    # path('edit-task/<int:task_id>/', edit_task, name='edit_task'),
    # path('delete-task/<int:task_id>/', delete_task, name='delete_task'),
    path('group/<int:group_id>/list/<int:list_id>/task/<int:task_id>/edit/', edit_task, name='edit_task'),
    path('group/<int:group_id>/list/<int:list_id>/task/<int:task_id>/delete/', delete_task, name='delete_task'),
    path('create-task/<int:id>/', create_task, name='create_task'),
    path('mark-as-incomplete/<int:task_id>/', mark_as_incomplete, name='mark_as_incomplete'),
    path('task/<int:task_id>/edit/', edit_task, name='edit_task'),
    path('task/<int:task_id>/delete/', delete_task, name='delete_task'),

]
