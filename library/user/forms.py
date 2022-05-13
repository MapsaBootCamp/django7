from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm

from .models import Profile


class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=255, required=True)
    password = forms.CharField(widget=forms.PasswordInput)

    # username.widget.attrs.update({'id': 'username', 'width': '50px'})


class CustomUserCreationForm(UserCreationForm):
    phone_number = forms.CharField(label="شماره تلفن", required=True)
    membership_expire_date = forms.DateField()
    
    class Meta:
        model = Profile
        fields = ['username',
                  'password1', 'password2', 'phone_number', 'membership_expire_date']
        labels = {
            "username": "یوزرنیم",
            "password1": "رمز عبور",
            "password2": "تکرار رمز عبور",

        }
        
        help_texts = {
            "email": "ایمیل خود را به درستی وارد کنید",
        }



class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = Profile
        fields = ('email', 'first_name')

