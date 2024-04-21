
from django import forms
from .models import House, Room




class HouseCreateForm(forms.ModelForm):
    class Meta:
        model = House
        fields = ["name","num_rooms","user"]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'num_rooms': forms.TextInput(attrs={'class': 'form-control'}),
            # '': forms.PasswordInput(attrs={'class': 'form-control'}, render_value=True)
        }
class RoomCreateForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = "__all__"