"""from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request, 'index.html')
    #return HttpResponse("Hello")
def add(request):
    return render(request, 'add.html')
    #return HttpResponse("Enter event details")
def display(request):
    return HttpResponse("display event details")
def Update(request):
    return HttpResponse("Update event details")"""""

from django.http import HttpResponse
from django.shortcuts import render
from .models import event_scheduler

def index(request):
    return render(request, 'index.html')
def add(request):
    x = event_scheduler.objects.all()
    if request.method == 'POST':
        name = request.POST['eventname']
        date = request.POST['birthday']
        time = request.POST['appt']
        description = request.POST['message']

        new_event = event_scheduler(name=name, date=date, time=time, description=description)
        new_event.save()
        return HttpResponse("Data Saved")
   # return render(request, 'add.html', {'x': x})
    return render(request, 'add.html')


def display(request):
    #x = event_scheduler.objects.all()
    if request.method == 'POST':
        name = request.POST['eventname']
        date = request.POST['birthday']
        time = request.POST['appt']
        description = request.POST['message']
        obj=event_scheduler()
        obj.name=name
        obj.date=date
        obj.time=time
        obj.description=description
        obj.save()
    from django.core import serializers
    data=serializers.serialize("python",event_scheduler.objects.all())
    context={
        'data':data,
    }
    return render(request, 'display.html',context)
    #return HttpResponse("display event details")


def Update(request):
    return HttpResponse("Update event details")





