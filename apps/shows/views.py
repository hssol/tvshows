from django.shortcuts import render, redirect
from .models import *

def shows(request):
    context = {
        "all_shows" : Show.objects.all()
    }
    return render(request, 'shows/index.html', context)

def new(request):
    return render(request, 'shows/new.html')

def add_show(request):
    if request.method == "POST":
        newShow = Show.objects.create(title=request.POST["title"], network=request.POST["network"], desc=request.POST["desc"])
    return redirect('/shows/{}'.format(newShow.id))

def display_show(request, id):
    context = {
        "show_info" : Show.objects.get(id=id)
    }
    return render(request, 'shows/show_display.html', context)

def edits(request, id):
    context = {
        "show_info" : Show.objects.get(id=id)
    }
    return render(request, 'shows/edit.html', context)

def edit_show(request, id):
    c = Show.objects.get(id=id)
    c.title = request.POST['title']
    c.network = request.POST['network']
    c.desc = request.POST['desc']
    c.save()
    return redirect('/shows/{}'.format(id))

def delete_show(request, id):
    c = Show.objects.get(id=id)
    c.delete()
    return redirect('/shows')