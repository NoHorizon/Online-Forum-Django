#custom
from django.urls import path #პროექტის urls, ამ შვემთხვევაში helpbuddy.urls.py
from . import views # '.' გულისხმობს ამ ფაილის სამყოფელ ფოლდერს ანუ: base.views

urlpatterns = [
    path('', views.home, name='home'), #მიიღო 3 პარამეტრი, მისამართი, ლოკაცია, სახელი,
    path('room_page/<str:pk>/', views.room, name='room'),
    #str - string
    #pk - primary key
]
