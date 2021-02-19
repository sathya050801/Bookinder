from django.shortcuts import render
from .models import Reader

# Create your views here.

def index(response):
    return render(response,'index.html',{})
