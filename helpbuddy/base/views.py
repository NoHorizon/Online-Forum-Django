from django.shortcuts import render

#custom
# from django.http import HttpResponse
from .models import Room
# Create your views here.
#custom

# def home(request):
#     return HttpResponse('Home Page, this text(function) location base/views.py"')

# def room(request):
#     return HttpResponse("ROOM, this text(function) location base/views.py")

# creating rooms, each room will have an id
# rooms = [
#     {'id': 1, 'name': 'Lets learn python'},
#     {'id': 2, 'name': 'Design with me'},
#     {'id': 3, 'name': 'Frontend developers'},
# ]


def home(request):
    rooms = Room.objects.all() #მოდელი
    context = {'rooms': rooms} # მიიღებს მხოლოდ 1-თს, ამიტომ მეორე list-ის არსებობის შემთხვევაში უნდა დავამატოთ ამავეში, მაგ: context = {'rooms': rooms, 'names': names და ა.შ}
    return render(request, 'base/home.html', context)

# def room(request, pk):
#     room = None #ანუ პირველად შესვლისას გვერდს არ ექნება ნომერი /room/'1'
#     for i in rooms:
#         if i['id'] == int(pk):
#             room = i
#     context = {'room' : room}
#     return render(request, 'base/room.html', context)

def room(request, pk):
    room = Room.objects.get(id=pk)
    context = {'room' : room}
    return render(request, 'base/room.html', context)