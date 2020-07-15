from django.shortcuts import render,redirect
from . models import Todo
from .forms import TodoForm
# Create your views here.


def index(request):
    form = TodoForm()
    todo = Todo.objects.order_by('id')

    if request.method=='POST':
        form = TodoForm(request.POST)
        if form.is_valid:
            todo = Todo(text=request.POST['text'])
            todo.save()
            return redirect('index')

    context = {
        'todo' : todo,
        'form': form
    }
    return render(request,'todo/index.html',context)


def completed(request,todo_id):
    todo = Todo.objects.get(pk=todo_id)
    todo.complete = True
    todo.save()
    return redirect('index')


def deletecompleted(request):
    Todo.objects.filter(complete__exact=True).delete()

    return redirect('index')


