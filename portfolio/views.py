from django.shortcuts import render

def home(request):
    return render(request, 'portfolio/index.html')
def projects(request):
    return render(request, 'portfolio/projects.html')

def about(request):
    return render(request, 'portfolio/about.html')