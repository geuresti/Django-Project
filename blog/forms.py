from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import *

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text',)

# doesn't work
class CustomUserRegistrationForm(forms.Form):
    username = models.CharField(max_length=15)
    email = models.EmailField(max_length=30)
    password1 = models.CharField(max_length=30)#, widget=forms.PasswordInput)
    password2 = models.CharField(max_length=30)#, widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise ValidationError("That username is already taken.")
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("That email is already being used.")
        return email

    def clean_password(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 != password2:
            raise ValidationError("Passwords don't match.")
        return password1

    def save(self, commit=True):
        user = User.objects.create_user(
            self.cleaned_data['username'],
            self.cleaned_data['email'],
            self.cleaned_data['password1']
        )
        return user

#    class Meta:
#        model = Account
#        fields = ('username', 'password', 'email',)
