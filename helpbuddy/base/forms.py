from django.forms import ModelForm
from .models import Room
from django.contrib.auth.models import User


class RoomForm(ModelForm):
    class Meta:
        model = Room
        # models.py დან იღებს კლასი Room-ის მონაცემებს
        # შეიძლება ლისთის სახითაც მაგ: ['name', 'body' და ა.შ]
        # fields = '__all__' # no need
        exclude = ['host', 'participants']


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']
