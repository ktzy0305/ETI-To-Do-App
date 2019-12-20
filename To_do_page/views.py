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
    if ((own!= "")and (new_todo!="")):
        time = datetime.now()
        #time = time.strftime('%Y-%m-%d %H:%M')
        new_item = ToDoItem(owner=own, Todo=new_todo, Timecreated=time)
        new_item.save()
        archiveHistory(own, new_todo, time, 'Added')
        return HttpResponseRedirect('/To_do_page/')
    else:
        #context["error"] = "Check your input for Owner name and Item name."
        #return {'some_flag': True}
        return render(request, 'to_do.html', {'some_flag': True})
        #return HttpResponseRedirect('/To_do_page/', {'some_flag': True})
    
def deleteTodo(request, todo_id, todo_own, todo_Todo):
    own = todo_own
    new_todo = todo_Todo
    time = datetime.now()
    delete_item = ToDoItem.objects.get(id=todo_id)
    delete_item.delete()
    archiveHistory(own, new_todo, time, 'Deleted')
    return HttpResponseRedirect('/To_do_page/')

def archiveHistory(todo_own, todo_Todo, timecreated, action):
    own = todo_own
    todo = todo_Todo
    time = timecreated
    act = action
    new_item = ArchiveHistory(owner=own, Todo=todo, Timecreated=time, action=act)
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
