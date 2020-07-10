from django import forms
class Registerform(forms.Form):
    name=forms.CharField(label='',widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Username'}))
    email=forms.EmailField(label='',widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder':'Email' }))
    password1=forms.CharField(label='', widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder':'Password'}))
    password2=forms.CharField(label='',widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder':'Confirm Password'}))
class loginform(forms.Form):
    name=forms.CharField(label='',widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Username'}))
    password1=forms.CharField(label='', widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder':'Password'}))