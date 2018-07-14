from django.shortcuts import render, redirect

from .models import Task, List


def home_page(request):
    if request.method == 'POST':
        list_ = List.objects.create()
        Task.objects.create(title=request.POST['title'], list=list_)
        return redirect(f'/lists/{list_.id}')

    return render(request, 'lists/home.html',)


def lists_show(request, list_id):
    return render(request, 'lists/lists_show.html', {
        'tasks': Task.objects.filter(list=List.objects.get(id=list_id)),
        'list_id': list_id,
    })


def lists_add_task(request, list_id):
    list_ = List.objects.get(id=list_id)
    Task.objects.create(title=request.POST['title'], list=list_)

    return redirect(f'/lists/{list_id}')
