"""ToDoApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from To_do_page.views import todoGreeting, addTodo, deleteTodo, logout_view, archiveHistory, historyItem
from contributions.views import contributions_view
from django.views.generic.base import TemplateView # new

urlpatterns = [
    path('admin/', admin.site.urls),
    path('To_do_page/', todoGreeting, name='todopage'),
    path('addTodo/', addTodo),
    path('deleteTodo/<int:todo_id>/', deleteTodo),
    path('logout_view/', logout_view),
    path('login/', include('django.contrib.auth.urls')),
    path('login/', TemplateView.as_view(template_name='home.html'), name='home'),
    path('archiveHistory/<todo_Todo>/<todo_own>/', archiveHistory),
    path('historyItem', historyItem),
    path('contribution/', contributions_view)
]
