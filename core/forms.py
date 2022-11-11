from django import forms
from core.models import ToDO

class DateInput(forms.DateInput):
    input_type = 'date'
    
class ToDOForm(forms.ModelForm):

    class Meta:
        model = ToDO
        fields = ['name','state','created_at']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),

            'created_at': DateInput(),
        }