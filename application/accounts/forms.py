from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class SignUpForm(UserCreationForm):
    username = forms.CharField(label="Login", max_length=30, required=True,
                               error_messages={'required': "This field is required!"})
    first_name = forms.CharField(label="First Name", max_length=30, required=True,
                                 error_messages={'required': "This field is required!"})
    last_name = forms.CharField(label="Last Name", max_length=30, required=True,
                                error_messages={'required': "This field is required!"})
    email = forms.EmailField(label="Email", max_length=254, required=True,
                             error_messages={'required': "This field is required!"})
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)