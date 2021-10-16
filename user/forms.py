from .admin import UserCreationForm
from .models import MyUser,Product,Order
from django.forms import ModelForm
from django import forms


class SignUpForm(UserCreationForm):
    password1=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:
        model=MyUser
        fields=['username','email','password1','password2']
        widgets={
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),

        }

class SignInForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))


class Order_form(ModelForm):
    class Meta:
        model=Order
        fields=['products','address','phone_number']

        widgets={
            'products':forms.Select(attrs={'type':'select','readonly':True,'class':'form-control'}),
            'address':forms.Textarea(attrs={'class':'form-control'}),
            'phone_number':forms.TextInput(attrs={'class':'form-control'})
        }

