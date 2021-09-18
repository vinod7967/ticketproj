from django import forms
from django.contrib.auth.models import User
from django import forms
from .models import EmployeeModel
from django.contrib.auth.forms import UserCreationForm
class SignupForm(UserCreationForm):
    password2 = forms.CharField(label='Confirm Password (again)', widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']
        labels = {'email':'Email'}
class EmployeeModelForm(forms.ModelForm):
    class Meta:
        model = EmployeeModel
        fields = ['Query']
        widget={
            "Query":forms.TextInput(attrs={"class": "form-control"})
        }
class AdminModelForm(forms.ModelForm):
    class Meta:
        model = EmployeeModel
        fields = ['status']

class form_status(forms.ModelForm):
    class Meta:
        model = EmployeeModel
        fields = '__all__'