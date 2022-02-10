from multiprocessing import context
import re
from django.http import HttpResponse,JsonResponse
from django.shortcuts import render,redirect
from .models import Room,Message
import datetime
from datetime import datetime,date
# Create your views here.
def home(request):
    return render(request,'home.html')

def room(request,room):
    username = request.GET.get('username')
    room_details= Room.objects.get(room=room)
    context ={
         'username':username,
         'room':room,
         'room_details' : room_details,
    }
    print(room_details)
    print(room)
    return render(request,'room.html',context)

def check(request):
    room = request.POST['room_name']
    username = request.POST['username']

    if Room.objects.filter(room=room).exists():
        return redirect('/'+room+'/?username='+username)
    else:
        new = Room.objects.create(room=room)
        new.save()
        return redirect('/'+room+'/?username='+username)


def send(request):
    message =request.POST['message']
    username =request.POST['username']
    room_id =request.POST['room_id']
    now = datetime.now()
    current_time = now.strftime("%I:%M:%S %p")
    today = date.today().strftime('%d/%m/%Y')
    new = Message.objects.create(value=message,user=username,room=room_id,date=today,time=current_time)
    new.save()
    return HttpResponse('message came successfully')

def getMessages(request, room):
    room_details = Room.objects.get(room=room)

    message = Message.objects.filter(room=room_details.id)
    return JsonResponse({"messages":list(message.values())})

def feedback(request):
    print('Checking MY answer Hello')
    return render(request,'feedback.html')