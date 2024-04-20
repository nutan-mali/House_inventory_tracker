
from django import forms
from .models import House, Room




class HouseCreateForm(forms.ModelForm):
    class Meta:
        model = House
        fields = "__all__"
   
class RoomCreateForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = "__all__"