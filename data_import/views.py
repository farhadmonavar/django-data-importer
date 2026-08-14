from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

def celery_test(request):
    return HttpResponse('<h3>Function executed successfully</h3>')