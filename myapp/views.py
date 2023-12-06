from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
# from .models import *
 # from .forms import OrderForm
# from .filters import OrderFilter

def index(request):
    return render(request, 'myapp/index.html',{})

def loginPage(request):
    context = {}
    return render(request, 'accounts/login.html', context)

def registerPage(request):
    form = UserCreationForm()
    context = {'form':form}
    return render(request, 'accounts/register.html', context)