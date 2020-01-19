from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm

from todos.models import Todo

class TodoForm(ModelForm):
    class Meta:
        model = Todo
        fields = ['item']

def home(request):
    return render(request, 'todos/base.html')

def todo_list(request, template_name="todos/todo_list.html"):
    todo = Todo.objects.all()
    data = {}
    data['object_list'] = todo
    return render(request, template_name, data)

def todo_view(request, pk, template_name="todos/todo_detail.html"):
    todo = get_object_or_404(Todo, pk=pk)
    return render(request, template_name, {'object':todo})

def todo_create(request, template_name="todos/todo_form.html"):
    form = TodoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('todo_list')
    return render(request, template_name, {'form':form})

def todo_update(request, pk, template_name="todos/todo_form.html"):
    todo = get_object_or_404(Todo, pk=pk)
    form = TodoForm(request.POST or None, instance=todo)
    if form.is_valid():
        form.save()
        return redirect('todo_list')
    return render(request, template_name, {'form': form})

def todo_delete(request, pk, template_name="todos/todo_confirm_delete.html"):
    todo = get_object_or_404(Todo, pk=pk)
    if request.method=='POST':
        todo.delete()
        return redirect('todo_list')
    return render(request, template_name, {'object':todo})
