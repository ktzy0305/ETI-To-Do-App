from django.shortcuts import render
from django.http import HttpResponseRedirect
from To_do_page.models import ToDoItem, ArchiveHistory
from django.contrib.auth import logout, get_user
from datetime import datetime

# Create your views here.

#def todoGreeting(request):
#    return HttpResponse('Hello, this is To-Do Page.')

def todoGreeting(request):
    own = get_user(request)
    all_todo = ToDoItem.objects.all().filter(owner=own)
    context = {
        'all_items': all_todo
    }
    return render(request, 'to_do.html', context)
    
def addTodo(request):
    own = get_user(request)
    new_todo = request.POST['Todo']
    time = datetime.now()
    #time = time.strftime('%Y-%m-%d %H:%M')
    new_item = ToDoItem(owner=own, Todo=new_todo, Timecreated=time)
    new_item.save()
    return HttpResponseRedirect('/To_do_page/')
    
def deleteTodo(request, todo_id):
    delete_item = ToDoItem.objects.get(id=todo_id)
    delete_item.delete()
    return HttpResponseRedirect('/To_do_page/')
    
def archiveHistory(request, todo_Todo, todo_own):
    own = todo_own
    todo = todo_Todo
    new_item = ArchiveHistory(owner=own, Todo=todo)
    new_item.save()
    return HttpResponseRedirect('/To_do_page/')
    
def historyItem(request):
    all_todo = ArchiveHistory.objects.all()
    context = {
        'all_items': all_todo
    }
    return render(request, 'history_page.html', context)
    
    
def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/login/login/')