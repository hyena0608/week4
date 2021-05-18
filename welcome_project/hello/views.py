from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def hello(request):
    userName = request.GET['user']
    return render(request, 'name.html',{'userName' : userName})