from django.db import models
from django.contrib.auth.models import User
from django import forms
# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, max_length=100)
    data = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=200)
    text = models.TextField()
    def __str__(self):
        return self.title

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="profile/", default="profile/default.jpg")

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']