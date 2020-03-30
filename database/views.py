from django.shortcuts import render

def home(request):
    return render(request, 'database/home.html')

def publications(request):
    return render(request, 'database/publications.html')

def presentations(request):
    return render(request, 'database/presentations.html')

