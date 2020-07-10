from django import forms
from .models import Orders

class Orderform(forms.ModelForm):
    class Meta:
        model=Orders
        fields=['address','phone_no']
        widgets={'address':forms.Textarea(attrs={'class': 'form-control'}),
                 'phone_no':forms.TextInput(attrs={'class': 'form-control'}),
             
            }

