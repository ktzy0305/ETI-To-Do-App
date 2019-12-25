import pytest
from ToDoApp.wsgi import *
from To_do_page.views import *
from django.test import Client
from django.urls import reverse
from To_do_page.models import ToDoItem

client = Client()

def test_to_do_page_view():
    response = client.get(reverse('todopage'))
    assert response.status_code == 200

def test_to_do_page_view_pagination():
    response = client.get(reverse('todopage'), {'page': 2})
    assert response.status_code == 200

def test_add_to_do_view():
    original_count = ToDoItem.objects.all().count()
    response = client.post(reverse('todopage'), {'Todo': 'Test Adding To-Do Item'})
    assert (ToDoItem.objects.all().count() == original_count + 1) and (response.status_code == 200)

def test_add_empty_to_do_view():
    original_count = ToDoItem.objects.all().count()
    response = client.post(reverse('todopage'), {'Todo': ''})
    assert (ToDoItem.objects.all().count() == original_count) and (response.status_code == 200)

def test_delete_to_do_view():
    original_count = ToDoItem.objects.all().count()
    latest_to_do_object = ToDoItem.objects.all().latest("id")
    response = client.get('/deleteTodo/{0}/{1}/{2}/'.format(latest_to_do_object.id, latest_to_do_object.owner, latest_to_do_object.Todo))
    assert (ToDoItem.objects.all().count() == original_count - 1) and (response.status_code == 302)

def test_to_do_history_view():
    response = client.get(reverse('todohistorypage'))
    assert response.status_code == 200

def test_to_do_history_view_pagination():
    response = client.get(reverse('todohistorypage'), {'page': 2})
    assert response.status_code == 200

def test_contribution_view():
    response = client.get(reverse('contributionpage'))
    assert response.status_code == 200   

def test_login_view():
    response = client.get(reverse('login'))
    assert response.status_code == 200   

def test_logout_view():
    response = client.get(reverse('logout'))
    assert response.status_code == 302   

def test_signup_view():
    response = client.get(reverse('signup'))
    assert response.status_code == 200