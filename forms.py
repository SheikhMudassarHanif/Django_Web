from django import forms
from regiterformapp.models import UserProfileInfo
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())


    class Meta():
        model=User
        fields=('username','email','password')


class UserProfileInfoForm(forms.ModelForm):
        portfolio_Link=forms.URLField(required=False)
        picture=forms.ImageField(required=False)
        class Meta():
            model=UserProfileInfo
            fields=('portfolio_Link','picture')
