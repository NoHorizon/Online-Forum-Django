from django.forms import ModelForm

from .models import Room


class RoomForm(ModelForm):
    class Meta:
        model = Room
        # models.py დან იღებს კლასი Room-ის მონაცემებს
        # შეიძლება ლისთის სახითაც მაგ: ['name', 'body' და ა.შ]
        fields = '__all__'
