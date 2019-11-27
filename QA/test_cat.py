import pytest
from ToDoApp.cat import *

def test_cat_meow():
    test_cat = Cat("Tom")
    assert test_cat.meow() == "Meow"