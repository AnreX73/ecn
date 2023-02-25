from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordResetForm
from django import forms
from django.core import validators
from django.utils.translation import gettext_lazy as _
from ckeditor.widgets import CKEditorWidget
from captcha.fields import CaptchaField

from ecn import models
from ecn.models import InCityObject, OutCityObject, Gallery
from imagekit.forms import ProcessedImageField
from imagekit.processors import ResizeToFill

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
    phone_number = forms.CharField(label='телефон для связи', max_length=15, required=True,
                                   widget=forms.TextInput(attrs={'class': 'form-input'}), )
    password1 = forms.CharField(label=_("password"), widget=forms.PasswordInput(attrs={'class': 'form-input'}), )
    password2 = forms.CharField(label='повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}), )
    captcha = CaptchaField(label='Введите текст с картинки')

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'first_name', 'phone_number')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-input'}),

        }


class ChangeUserlnfoForm(forms.ModelForm):
    phone_number = forms.CharField(label='телефон для связи', max_length=30, required=True,
                                   widget=forms.TextInput(attrs={'class': 'form-input'}), )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'first_name', 'phone_number')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-input'}),
            'email': forms.EmailInput(attrs={'class': 'form-input'}),
            'first_name': forms.TextInput(attrs={'class': 'form-input'}),

        }


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class': 'form-input'}), )
    password = forms.CharField(label=_("password"), widget=forms.PasswordInput(attrs={'class': 'form-input'}), )
    # captcha = CaptchaField(label='Введите текст с картинки')


class UserPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(
        label=_("Email"),
        max_length=254,
        widget=forms.EmailInput(attrs={"autocomplete": "email", 'class': 'form-input'}),
    )


class InCitySearchForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['city_region'].empty_label = 'все районы'
        self.fields['object_type'].empty_label = 'все предложения'
        self.fields['rooms'].empty_label = 'любое'
        self.fields['rooms'].required = False
        self.fields['city_region'].required = False
        self.fields['object_type'].required = False

    class Meta:
        model = InCityObject
        fields = ('sale_or_rent', 'object_type', 'city_region', 'rooms')


class InCityAddForm(forms.ModelForm):
    slug = forms.CharField(widget=forms.HiddenInput, label='')
    is_hot = forms.CharField(widget=forms.HiddenInput, label='')
    is_published = forms.CharField(widget=forms.HiddenInput, label='')
    estate_agent = forms.ModelChoiceField(queryset=User.objects.all(),
                                          widget=forms.HiddenInput, label='')
    content = forms.CharField(widget=CKEditorWidget, label='Текстовое описание')
    image = ProcessedImageField(spec_id='ecn:media:ecn_thumbnail',
                                label='Основное изображение',
                                processors=[ResizeToFill(1200, 900)],
                                format='JPEG',
                                options={'quality': 70})

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['slug'].required = False
        self.fields['is_hot'].required = False
        self.fields['is_published'].required = False

    class Meta:
        model = InCityObject
        fields = '__all__'


class InCityUpdateForm(InCityAddForm):
    image = ProcessedImageField(spec_id='ecn:media:ecn_thumbnail',
                                label='Изменить изображение',
                                processors=[ResizeToFill(1200, 900)],
                                format='JPEG',
                                options={'quality': 70},
                                validators=[
                                    validators.FileExtensionValidator(allowed_extensions=('gif', 'jpg', 'png'))],
                                error_messages={'invalid_extension': 'Этот формат не поддерживается'},
                                widget=forms.widgets.FileInput)


class OutCityAddForm(InCityAddForm):
    land_square = forms.CharField(label='Участок в сотках')

    class Meta:
        model = OutCityObject
        fields = '__all__'


class OutCityUpdateForm(OutCityAddForm):
    image = forms.ImageField(label='Изменить основное фото',
                             validators=[validators.FileExtensionValidator(allowed_extensions=('gif', 'jpg', 'png'))],
                             error_messages={'invalid_extension': 'Этот формат не поддерживается'},
                             widget=forms.widgets.FileInput)


class PhotoAddForm(forms.ModelForm):
    gallery_image = ProcessedImageField(spec_id='ecn:media:ecn_thumbnail',
                                        label='Добавить  изображение',
                                        processors=[ResizeToFill(1200, 900)],
                                        format='JPEG',
                                        options={'quality': 70},
                                        validators=[
                                            validators.FileExtensionValidator(
                                                allowed_extensions=('gif', 'jpg', 'png'))],
                                        error_messages={'invalid_extension': 'Этот формат не поддерживается'},
                                        widget=forms.widgets.FileInput)
    galleryLink = forms.ModelChoiceField(queryset=InCityObject.objects.all(),
                                         widget=forms.HiddenInput, label='')
    is_published = forms.CharField(widget=forms.HiddenInput, label='')

    class Meta:
        model = Gallery
        fields = '__all__'




