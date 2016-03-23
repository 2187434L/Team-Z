from django import forms
from django.contrib.auth.models import User
from ChineseFoodRank.models import Food,UserProfile

class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=128, help_text="Please enter the category name.")
    # slug = forms.CharField(widget=forms.HiddenInput(), required=False)
    # An inline class to provide additional information on the form.

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'email', 'password',)

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('website', 'picture')

