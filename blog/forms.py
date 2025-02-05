from django import forms
from .models import Posts, Users

class PostForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ['title', 'content']

class UserForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ['first_name','last_name','email', 'password']

     
class LoginForm(forms.Form):
    username = forms.CharField(max_length=200)
    password = forms.CharField(max_length=200)