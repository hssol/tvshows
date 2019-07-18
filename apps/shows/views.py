from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages

def shows(request):
    if 'activeuser' not in request.session:
        return redirect('/')
    else:
        context = {
            "all_shows" : Show.objects.all()
        }
        return render(request, 'shows/index.html', context)

def new(request):
    if 'activeuser' not in request.session:
        return redirect('/')
    else:
        return render(request, 'shows/new.html')

def add_show(request):
    if 'activeuser' not in request.session:
        return redirect('/')
    else:
        errors = Show.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/shows/new')
        else:
            newShow = Show.objects.create(title=request.POST["title"], network=request.POST["network"], desc=request.POST["desc"])
        return redirect('/shows/{}'.format(newShow.id))

def display_show(request, id):
    if 'activeuser' not in request.session:
        return redirect('/')
    else:
        context = {
            "show_info" : Show.objects.get(id=id)
        }
        return render(request, 'shows/show_display.html', context)

def edits(request, id):
    if 'activeuser' not in request.session:
        return redirect('/')
    else:
        context = {
            "show_info" : Show.objects.get(id=id)
        }
        return render(request, 'shows/edit.html', context)

def edit_show(request, id):
    if 'activeuser' not in request.session:
        return redirect('/')
    else:
        errors = Show.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/shows/{}/edit'.format(id))
        else:
            show = Show.objects.get(id = id)
            show.title = request.POST['title']
            show.network = request.POST['network']
            show.desc = request.POST['desc']
            show.save()
            messages.success(request, "Show information successfully updated")
            return redirect('/shows')


def delete_show(request, id):
    if 'activeuser' not in request.session:
        return redirect('/')
    else:
        c = Show.objects.get(id=id)
        c.delete()
        return redirect('/shows')

def logout(request):
    request.session.clear()
    return redirect('/')