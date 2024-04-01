from django.contrib.auth.forms import UserCreationForm , UserChangeForm
from .models import CustomUser, Seller, SellerAdditional
from django import forms


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model =CustomUser
        fields = ('email',)

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('email',)

class RegistrationForm(UserCreationForm): 
    class Meta:
        model = Seller
        fields = [
            'email',
            'name',
            'password1',
            'password2',
        ]

class RegistrationFormSeller(UserCreationForm):
    gst = forms.CharField(max_length=10)
    warehouse_location = forms.CharField(max_length=1000)
    class Meta:
        model = Seller
        fields = [
            'email',
            'name',
            'password1',
            'password2',
            'gst',
            'warehouse_location'
        ]

class RegistrationFormSeller2(forms.ModelForm):
    class Meta:
        model = SellerAdditional
        fields = [
            'gst',
            'warehouse_location'
        ]