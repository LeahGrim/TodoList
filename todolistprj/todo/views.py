from django.shortcuts import render
from django.http import HttpResponse 
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.urls import reverse_lazy
from .models import Task

class TaskList(ListView):
    model = Task 
    # rename context object name to use task in the html in the for loop
    context_object_name = 'task' 

class TaskDetail(DetailView):
    model = Task 
    context_object_name = 'task'
    template_name = 'todo/task.html'


class TaskCreate(CreateView):
    model = Task
    # this will show all the fields that we have created in models.py
    fields = "__all__"
    # after creating new task, user will be brought to new page
    success_url = reverse_lazy('task')


class TaskUpdate(UpdateView):
    model = Task 
    fields = "__all__"
    success_url = reverse_lazy('task')

class TaskDelete(DeleteView):
    model = Task
    context_object_name= 'task'
    