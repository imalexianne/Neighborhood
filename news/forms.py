from django.contrib.auth.forms import UserCreationForm
from .models import User,Post, Profile, Village,Business,Health,Police,Guest
from django import forms
 
class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email','password')

class VillageForm(forms.ModelForm):
    class Meta:
        model= Village
        fields = ('name','location','occupants','characteristics')

class BusinessForm(forms.ModelForm):
    class Meta:
        model= Business
        exclude = ['user']

class PostForm(forms.ModelForm):
    class Meta:
        model= Post
        exclude = ['user']


class ProfileForm(forms.ModelForm):
    class Meta:
        model= Profile
        exclude = ['user']

class HealthForm(forms.ModelForm):
    class Meta:
        model= Health
        exclude = ['user']

class PoliceForm(forms.ModelForm):
    class Meta:
        model= Police
        exclude = ['user']

class GuestForm(forms.ModelForm):
    class Meta:
        model= Guest
        exclude = ['user']


