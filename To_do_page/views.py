from django.shortcuts import render
from django.http import HttpResponseRedirect
<<<<<<< HEAD
from To_do_page.models import ToDoItem
=======
from To_do_page.models import ToDoItem, ArchiveHistory
from django.contrib.auth import logout, get_user
from datetime import datetime

>>>>>>> 406db8e41e9f4c4cd75a88ea58055b45a9551e8a

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
        return HttpResponseRedirect('/To_do_page/')
    else:
        #context["error"] = "Check your input for Owner name and Item name."
        #return {'some_flag': True}
        return render(request, 'to_do.html', {'some_flag': True})
        #return HttpResponseRedirect('/To_do_page/', {'some_flag': True})
    
def deleteTodo(request, todo_id):
    delete_item = ToDoItem.objects.get(id=todo_id)
    delete_item.delete()
    return HttpResponseRedirect('/To_do_page/')