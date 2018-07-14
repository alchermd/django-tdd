from django.shortcuts import render, redirect

from .models import Task


def home_page(request):
    if request.method == 'POST':
        Task.objects.create(title=request.POST['title'])
        return redirect('/lists/foobar')

    return render(request, 'lists/home.html',)


def lists_show(request):
    return render(request, 'lists/lists_show.html', {
        'tasks': Task.objects.all(),
    })
