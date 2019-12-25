import pytest
from ToDoApp.wsgi import *
from To_do_page.models import ToDoItem, ArchiveHistory
from datetime import datetime

def test_retrieve_to_do_items():
    to_do_items = ToDoItem.objects.all()
    assert to_do_items.count() > 0

def test_to_do_item_model():
    new_item = ToDoItem(owner="Tester", Todo="Test this application", Timecreated=datetime.now())
    new_item.save()
    latest_item = ToDoItem.objects.all().latest('id')
    assert latest_item.Todo == new_item.Todo

def test_retrieve_archive_history_items():
    history_items = ArchiveHistory.objects.all()
    assert history_items.count() > 0

def test_to_do_item_model_action():
    new_history_item = ArchiveHistory(owner="Tester", Todo="Test this application's history", Timecreated=datetime.now(), action="Added")
    new_history_item.save()
    latest_item = ArchiveHistory.objects.all().latest('id')
    assert latest_item.Todo == new_history_item.Todo and latest_item.action == new_history_item.action