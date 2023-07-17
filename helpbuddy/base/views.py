from django.shortcuts import render, redirect
# custom
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# იმისათვის რომ არარეგისტირებულმა მომხარებელმა ვერ შეძლოს შექმნას 'ოთახი' ( @login_required იწერება ფუნქციის თავზე)
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .models import Room, Topic
from .forms import RoomForm


def loginPage(request):

    page = 'login'

    # თუ იუზერი უკვე დალოგინებულია გადავამისამართოთ მთავარ გვერდზე
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        # ვიღებთ იუზერს და პაროლს
        username = request.POST.get('username').lower()
        password = request.POST.get('password')
        # ვამოწმებს იუზერს და პაროლს
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')

        # ვადარებთ შეყვანილს და დარეგისტრირებულს
        user = authenticate(request, username=username, password=password)

        # თუ იუზერი არაა ცარიელი, ვალოგინებთ და იქმნება ახალი სესსია და ვამისამართებთ მთავარ გვერდზე
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username OR Password does not exist')

    context = {'page': page}
    return render(request, 'base/login_register.html', context)


def registerPage(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(
                request, 'Username already exists or passwords doesn\'t match')
    return render(request, 'base/login_register.html', {'form': form})


def logoutUser(request):
    logout(request)
    return redirect('home')


def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    rooms = Room.objects.filter(
        Q(topic__name__icontains=q) |
        Q(name__icontains=q) |
        Q(description__icontains=q)
    )  # მოდელი

    topics = Topic.objects.all()
    room_count = rooms.count()

    context = {'rooms': rooms, 'topics': topics, 'room_count': room_count}
    return render(request, 'base/home.html', context)


def room(request, pk):
    room = Room.objects.get(id=pk)
    context = {'room': room}
    return render(request, 'base/room.html', context)


# გვაქვს დაიმპორტებული, ამის ქვეშ რაც არის ხდება სავალდებულო
@login_required(login_url='login')
def createRoom(request):
    form = RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'base/room_form.html', context)


@login_required(login_url='login')
def updateRoom(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)

    if request.user != room.host:
        return HttpResponse('You are not the owner of this room')

    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}

    return render(request, 'base/room_form.html', context)


@login_required(login_url='login')
def deleteRoom(request, pk):
    room = Room.objects.get(id=pk)

    if request.user != room.host:
        return HttpResponse('You are not the owner of this room')

    if request.method == 'POST':
        room.delete()
        return redirect('home')
    return render(request, 'base/delete.html', {'obj': room})
