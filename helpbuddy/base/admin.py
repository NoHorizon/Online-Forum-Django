from django.contrib import admin

# Register your models here.
# custom

from .models import Room, Topic, Message  # ჩვენი შექმილი მოდელის იმპორტი ადმინპანელში (line1)
admin.site.register(Room)  # (line2)
admin.site.register(Topic)
admin.site.register(Message)