from django.shortcuts import render
from django.contrib.auth.decorators import login_required 

from .models import Room
# Create your views here.

@login_required
def rooms(request):
    rooms = Room.objects.all()
    for i in rooms:
        print(i)

    return render(request, 'room/rooms.html', {'rooms': rooms})

@login_required
def room(request, slug):
    room = Room.objects.get(slug=slug)
    print(request.user)
    return render(request, 'room/room.html', {'room':room})