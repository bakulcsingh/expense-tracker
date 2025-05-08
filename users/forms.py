from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['currency', 'profile_picture']
        
    def __init__(self, *args, **kwargs):
        super(ProfileUpdateForm, self).__init__(*args, **kwargs)
        
        # Currency choices
        CURRENCY_CHOICES = [
            ('USD', 'US Dollar ($)'),
            ('EUR', 'Euro (€)'),
            ('GBP', 'British Pound (£)'),
            ('JPY', 'Japanese Yen (¥)'),
            ('CAD', 'Canadian Dollar (C$)'),
            ('AUD', 'Australian Dollar (A$)'),
            ('INR', 'Indian Rupee (₹)'),
            ('CNY', 'Chinese Yuan (¥)'),
            ('BRL', 'Brazilian Real (R$)'),
            ('MXN', 'Mexican Peso (Mex$)'),
        ]
        
        self.fields['currency'] = forms.ChoiceField(choices=CURRENCY_CHOICES)