from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse('<h4>You are viewing:</h4> <h1>Django Project <i>yproj</i> Home Page</h1> <h5><br>Source: <i>yproj/views.py</i></h5>')

def about(request):
    return HttpResponse('<h4>You are viewing:</h4> <h1>Django Project <i>yproj</i> About Page</h1> <h5><br>Source: <i>yproj/views.py</i></h5>')