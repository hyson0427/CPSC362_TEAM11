from django.forms import ModelForm
from .models import Room, Comments

class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'

class CommentForm(ModelForm):
    class Meta:
        model = Comments
        fields = '__all__'