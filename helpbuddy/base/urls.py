# custom
from django.urls import path  # პროექტის urls, ამ შვემთხვევაში helpbuddy.urls.py
from . import views  # '.' გულისხმობს ამ ფაილის სამყოფელ ფოლდერს ანუ: base.views

urlpatterns = [
    # მიიღო 3 პარამეტრი, მისამართი, ლოკაცია, სახელი,
    path('', views.home, name='home'),
    path('room_page/<str:pk>/', views.room, name='room'),
    # str - string
    # pk - primary key

    path('create-room/', views.createRoom, name='create-room'),
    path('update-room/<str:pk>', views.updateRoom, name='update-room'),
    path('delete-room/<str:pk>', views.deleteRoom, name='delete-room'),

    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
]
