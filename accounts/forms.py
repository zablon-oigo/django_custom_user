from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import CustomUser
from django.contrib.auth import get_user_model

User=get_user_model()
class LoginForm(forms.Form):
    email=forms.EmailField(widget=forms.EmailInput(attrs={
        'placeholder':'enter valid email address'
    }))
    password=forms.CharField(widget=forms.PasswordInput(attrs={
        'placholder':'Enter password'
    }))
class CustomUserCreationForm(UserCreationForm):
    password1=forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Enter password'
    }))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Confirm password'
    }))

    class Meta:
        model=CustomUser
        fields=['username','email','password1','password2']

    def clean_password(self):
        cd=self.cleaned_data
        if cd['password2']!= cd['password1']:
            raise forms.ValidationError("password didn\t match ..")
        return cd['password2']
    
    def clean_email(self):
        data=self.cleaned_data['email']
        qs=User.objects.exclude(id=self.instance.id).filter(email=data)
        if qs.exists():
            raise forms.ValidationError('Email is in use..')
        return data
    
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model=CustomUser
        fields=['email']

        def clean_password(self):
        # Regardless of what the user provides, return the initial value.  
        # This is done here, rather than on the field, because the  
        # field does not have access to the initial value 
            return self.initial['password1']