from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordResetForm
from django import forms
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class UserCreationForm(UserCreationForm):
    email = forms.EmailField(
        label=_("Email"),
        max_length=254,
        widget=forms.EmailInput(attrs={"autocomplete": "email", 'class': 'form-input'}),
    )
    first_name = forms.CharField(label=_("first name"), max_length=150, required=True,
                                 help_text='Как к Вам обращаться?',
                                 widget=forms.TextInput(attrs={'class': 'form-input'}), )
    phone_number = forms.CharField(label='телефон для связи', max_length=150, required=True,
                                   widget=forms.TextInput(attrs={'class': 'form-input'}), )
    password1 = forms.CharField(label=_("password"),widget=forms.PasswordInput(attrs={'class': 'form-input'}),)
    password2 = forms.CharField(label='повтор пароля',widget=forms.PasswordInput(attrs={'class': 'form-input'}),)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'first_name', 'phone_number')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-input'}),
            
        }


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(max_length=150,widget=forms.TextInput(attrs={'class': 'form-input'}),)
    password = forms.CharField(label=_("password"), widget=forms.PasswordInput(attrs={'class': 'form-input'}), )


class UserPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(
        label=_("Email"),
        max_length=254,
        widget=forms.EmailInput(attrs={"autocomplete": "email", 'class': 'form-input'}),
    )

