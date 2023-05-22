from django.shortcuts import render, redirect
from django.http import HttpResponse 
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Task

class TaskList(LoginRequiredMixin, ListView):
    model = Task 
    # rename context object name to use task in the html in the for loop
    context_object_name = 'task' 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # filter the list of tasks for each user individually
        context['task'] = context['task'].filter(user=self.request.user)
        # check for complete and incomplete tasks, incomplete tasks to be loaded at the top
        context['count'] = context['task'].filter(complete= False).count()

        # logic that receives a string from the search input on task_list.html and filters tasks by user inputs  
        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['task'] =context['task'].filter(title__startswith = search_input)
            context['search_input'] = search_input

        return context
class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task 
    context_object_name = 'task'
    template_name = 'todo/task.html'


class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    # this will show all the fields that we have created in models.py
    fields = ['title', 'description','complete']
    # after creating new task, user will be brought to new page
    success_url = reverse_lazy('task')

    def form_valid(self, form):
        form.instance.user = self.request.user 
        return super(TaskCreate, self).form_valid(form)


class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task 
    fields = ['title', 'description','complete']
    success_url = reverse_lazy('task')

class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name= 'task'
    success_url = reverse_lazy('task')
    
class CustomLoginView(LoginView):
    template_name = 'todo/login.html'
    fields = "__all__"
    redirect_authenticated_user = False 

    def get_success_url(self): 
        return reverse_lazy('task')


class RegisterPage(FormView):
    template_name = 'todo/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user= True
    success_url = reverse_lazy('task')

    def form_valid(self, form ):
        user = form.save()
        # if we have a user, they will be logged in
        if user is not None: 
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated: 
            return redirect('task')
        return super(RegisterPage, self).get(*args, **kwargs)