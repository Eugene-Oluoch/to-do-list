from django.shortcuts import render,redirect
from .forms import TaskForm
from .models import Task
# Create your views here.


def home(request):
    form = TaskForm()
    tasks = Task.objects.all()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request,'index.html',{"form":form,"tasks":tasks})


def delete(request, id):
    task = Task.objects.get(id=id)
    task.delete()
    return redirect('home')


def edit(request, id):
    task = Task.objects.get(id=id)
    form = TaskForm(instance=task)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save(commit=False)
            task.name = request.POST.get('name')
            form.save()
            return redirect('home')
    return render(request,'edit.html',{"task":task,"form":form})


def clear(request):
    Task.objects.all().delete()
    return redirect('home')