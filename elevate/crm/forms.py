
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from django.forms.widgets import PasswordInput, TextInput
from .models import FirmDetails
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())

class FirmDetailsForm(forms.ModelForm):
    class Meta:
        model = FirmDetails
        fields = ['firm_name', 'mobile_no', 'address', 'gstn_no', 'msme_status', 'certification_name', 'firm_pdf']
        widgets = {
            'msme_status': forms.CheckboxInput(),
        }

    def clean(self):
        cleaned_data = super().clean()
        msme_status = cleaned_data.get("msme_status")
        certification_name = cleaned_data.get("certification_name")

        if msme_status and not certification_name:
            self.add_error('certification_name', "This field is required if MSME status is Yes.")
        return cleaned_data