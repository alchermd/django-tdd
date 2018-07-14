from django.shortcuts import render, redirect

from .models import Task

def home_page(request):
    if request.method == 'POST':
        Task.objects.create(title=request.POST['title'])
        return redirect('/')

    return render(request, 'lists/home.html', {
        'tasks': Task.objects.all(),
    })