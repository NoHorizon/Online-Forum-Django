from django.db import models

# Create your models here.
# custom
from django.contrib.auth.models import User #მაგალითად ადმინი, სხვა იუზერი

# მოდელის შექმნის მერე აუცილებელია მიგრაციის გაკეთება (python manage.py makemigrations და py manage.py migrate)


class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(
        Topic, on_delete=models.SET_NULL, null=True)  # Topic CLASS-ი
    name = models.CharField(max_length=200)
    # აქ null=True ნიშნავს, რომ ამ ველს შეუძლია იყოს ცარიელი და blank=True ანუ ფორმა შეიძლება იყოს ცარიელი
    description = models.TextField(null=True, blank=True)
    # participants =
    updated = models.DateTimeField(auto_now=True)  # ინახავს დროს ყოველ ჯერზე
    # ინახავს დროს მხოლოდ მაშინ როდესაც შეიქმნა
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created'] # - ნიშნავს ascended order, ანუ ახალი პოსტი იქნება ბოლოში, - gareshe descended order

    def __str__(self):
        return self.name


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[0:50]  # პირველი 50 სიმბოლო
