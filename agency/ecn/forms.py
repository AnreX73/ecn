from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class UserCreationForm(UserCreationForm):
    email = forms.EmailField(
        label=_("Email"),
        max_length=254,
        widget=forms.EmailInput(attrs={"autocomplete": "email"}),
    )
    first_name = forms.CharField(label=_("first name"), max_length=150, required=True,
                                 help_text='Как к Вам обращаться?'),
    phone_number = forms.CharField(label='телефон для связи', max_length=150, required=True,)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'first_name', 'phone_number')
