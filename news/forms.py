from django.contrib.auth.forms import UserCreationForm
from .models import User,Post, Profile, Neighborhood,Business,Health,Police
from django import forms
 
class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email','password')

class NeighborhoodForm(forms.ModelForm):
    class Meta:
        model= Neighborhood
        fields = ('name','location','occupants','characteristics')

class BusinessForm(forms.ModelForm):
    class Meta:
        model= Business
        exclude = ['user','neighborhood']

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
        exclude = ['neighborhood']

class PoliceForm(forms.ModelForm):
    class Meta:
        model= Police
        exclude = ['neighborhood']


