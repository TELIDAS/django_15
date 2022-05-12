from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from .models import CustomUser


class RegistrationForm(UserCreationForm):
    GENDER_TYPE = (
        ("MALE", "Male"),
        ("FEMALE", "Female"),
        ("OTHER", "Other")
    )
    OCCUPATION_CHOICE = (
        ("STUDENT", "STUDENT"),
        ("WORKER", "WORKER"),
        ("JOBLESS", "JOBLESS"),
        ("RETIRED", "RETIRED"),
    )
    gender = forms.ChoiceField(choices=GENDER_TYPE, required=True)
    occupation = forms.ChoiceField(choices=OCCUPATION_CHOICE, required=True)
    email = forms.EmailField(required=True)
    address = forms.CharField(required=True)

    class Meta:
        model = CustomUser
        fields = [
            "username",
            "email",
            "password1",
            "password2",
            "first_name",
            "last_name",
            "gender",
            "occupation",
            "address"
        ]

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)

    username = UsernameField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "type username",
                "id": "username"
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "type password",
                "id": "password"
            }
        )
    )
