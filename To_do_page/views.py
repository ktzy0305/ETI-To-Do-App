from django.shortcuts import render
from django.http import HttpResponseRedirect
from To_do_page.models import ToDoItem, ArchiveHistory
from django.contrib.auth import logout, get_user
from django.core.paginator import Paginator
from datetime import datetime


# Create your views here.

#def todoGreeting(request):
#    return HttpResponse('Hello, this is To-Do Page.')

def todoGreeting(request):
    context = {}
    if request.POST:
        owner_name = get_user(request)
        new_todo = request.POST['Todo']
        if ((owner_name != "")  and (new_todo != "")):
            addTodo(request, owner_name=owner_name, new_todo=new_todo)
        else:
            context['some_flag'] = True

    own = get_user(request)
    all_todo = ToDoItem.objects.all().filter(owner=own).order_by('-Timecreated')
    paginator = Paginator(all_todo, 5)
    page = request.GET.get('page')
    if page is not None:
        all_todo = paginator.get_page(page)
        context['all_items'] = all_todo
    else:
        all_todo = paginator.get_page(1)
        context['all_items'] = all_todo

    return render(request, 'to_do.html', context)
    
def addTodo(request, owner_name, new_todo):
    # own = get_user(request)
    # new_todo = request.POST['Todo']
    # if ((own!= "")and (new_todo!="")):
    #     time = datetime.now()
    #     #time = time.strftime('%Y-%m-%d %H:%M')
    new_item = ToDoItem(owner=owner_name, Todo=new_todo, Timecreated=datetime.now())
    new_item.save()
    archiveHistory(todo_own = new_item.owner, todo_Todo=new_item.Todo, timecreated=datetime.now(), action='Added')
    # return HttpResponseRedirect('/To_do_page/')
    # else:
        #context["error"] = "Check your input for Owner name and Item name."
        #return {'some_flag': True}
        # return render(request, 'to_do.html', {'some_flag': True})
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
    # return HttpResponseRedirect('/To_do_page/')

def historyItem(request):
    all_todo = ArchiveHistory.objects.all().order_by('-Timecreated')
    context = {
        'all_items': all_todo
    }
    paginator = Paginator(all_todo, 5)
    page = request.GET.get('page')
    if page is not None:
        all_todo = paginator.get_page(page)
        context['all_items'] = all_todo
    else:
        all_todo = paginator.get_page(1)
        context['all_items'] = all_todo
    return render(request, 'history_page.html', context)

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/login/login/') 
