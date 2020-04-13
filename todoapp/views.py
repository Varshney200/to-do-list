from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import TodoItem
# Create your views here.

def todoView(request):
    all_todo_items=TodoItem.objects.all().order_by('deadline')
    return render(request,'index2.html',{'all_items':all_todo_items})

def addToDo(request):
    new_item=TodoItem(content = request.POST['content'])
    new_item.deadline=request.POST['deadline']
    new_item.save()
    return HttpResponseRedirect('/todo/')

def deleteTodo(request, todo_id):
    delete_item = TodoItem.objects.get(id=todo_id)
    delete_item.delete()
    return HttpResponseRedirect('/todo/')

def clearList(request):
    TodoItem.objects.all().delete()
    return HttpResponseRedirect('/todo/')