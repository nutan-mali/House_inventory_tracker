
from django import forms
from .models import House, Room




class HouseCreateForm(forms.ModelForm):
    class Meta:
        model = House
        fields = ["name","num_rooms","user"]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'num_rooms': forms.TextInput(attrs={'class': 'form-control'}),
            
        }
class RoomCreateForm(forms.ModelForm):
    class Meta:
        model = Room
        house = forms.ModelChoiceField(queryset=House.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))

        fields =['house','name','equipment_name','purchase_date','maintenance_schedule','maintenance_date','discard_date','insurance_policy_number']

        widgets = {

            # 'house': forms.TextInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'equipment_name': forms.TextInput(attrs={'class': 'form-control'}),
            'purchase_date': forms.TextInput(attrs={'class': 'form-control'}),
            'maintenance_schedule': forms.TextInput(attrs={'class': 'form-control'}),
            'maintenance_date' :  forms.TextInput(attrs={'class': 'form-control'}),
            'discard_date': forms.TextInput(attrs={'class': 'form-control'}),
            'insurance_policy_number': forms.TextInput(attrs={'class': 'form-control'}),
           
        }