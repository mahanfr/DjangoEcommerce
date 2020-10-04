from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from .models import Profile

class UserRrgisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['first_name','last_name','username','email','password1','password2']


class UserProfileForm(forms.ModelForm):
    provice = forms.CharField(required=True)
    city = forms.CharField(required=True)
    address = forms.Textarea()
    postCode = forms.CharField(required=True)
    phonenumber = forms.CharField(required=True)
    cardNumber = forms.CharField(required=True)
    
    def clean_phonenumber(self):
        data = self.cleaned_data.get('phonenumber')
        if not len(data) == 11 or not data.isdigit():
            raise forms.ValidationError('شماره تلفن باید یازده رقمی باشد')
        if not data[0] == '0' or not data[1] == '9':
            raise forms.ValidationError('شماره تلفن اشتباه است')
        return data

    class Meta:
        model = Profile
        fiels = '__all__'
        exclude = ('score','user')