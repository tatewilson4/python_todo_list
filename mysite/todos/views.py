from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from todos.models import Todo

class TodoList(ListView):
    model = Todo

class TodoView(DetailView):
    model = Todo

class TodoCreate(CreateView):
    model = Todo
    fields = ['item']
    success_url = reverse_lazy('todo_list')

class TodoUpdate(UpdateView):
    model = Todo
    fields = ['item']
    success_url = reverse_lazy('todo_list')

class TodoDelete(DeleteView):
    model = Todo
    success_url = reverse_lazy('todo_list')
