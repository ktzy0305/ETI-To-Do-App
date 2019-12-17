from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import logout
from django.shortcuts import redirect


# Create your views here.

def contributions_view(request):
    return render(request, 'contribution_index.html')