from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordResetForm
from django import forms
from django.core import validators
from django.core.exceptions import ValidationError
from django.forms import inlineformset_factory
from django.utils.translation import gettext_lazy as _
from ckeditor.widgets import CKEditorWidget
from captcha.fields import CaptchaField

from ecn import models
from ecn.models import InCityObject, OutCityObject, Gallery, Gallery2
from imagekit.forms import ProcessedImageField

from pilkit.lib import Image

User = get_user_model()


class Resize(object):
    """
    Resizes an image to the specified width and height.

    """

    def __init__(self, width, height, upscale=True):
        """
        :param width: The target width, in pixels.
        :param height: The target height, in pixels.
        :param upscale: Should the image be enlarged if smaller than the dimensions?

        """
        self.width = width
        self.height = height
        self.upscale = upscale

    def process(self, img):
        if self.upscale or (self.width < img.size[0] and self.height < img.size[1]):
            img = img.convert('RGBA')
            img = img.resize((self.width, self.height), Image.ANTIALIAS)
        return img


class ResizeToCover(object):
    """
    Resizes the image to the smallest possible size that will entirely cover the
    provided dimensions. You probably won't be using this processor directly,
    but it's used internally by ``ResizeToFill`` and ``SmartResize``.

    """

    def __init__(self, width, height, upscale=True):
        """
        :param width: The target width, in pixels.
        :param height: The target height, in pixels.

        """
        self.width, self.height = width, height
        self.upscale = upscale

    def process(self, img):
        original_width, original_height = img.size

        if original_width < original_height:
            self.width, self.height = self.height, self.width
            print(self.width, self.height, original_width, original_height)

        ratio = max(float(self.width) / original_width,
                    float(self.height) / original_height)
        new_width, new_height = (int(round(original_width * ratio)),
                                 int(round(original_height * ratio)))
        print(new_width, new_height)
        img = Resize(new_width, new_height, upscale=self.upscale).process(img)
        print(img.width, img.height)
        return img


class ResizeToFill(object):
    """
    Resizes an image, cropping it to the exact specified width and height.

    """

    def __init__(self, width=None, height=None, anchor=None, upscale=True):
        """
        :param width: The target width, in pixels.
        :param height: The target height, in pixels.
        :param anchor: Specifies which part of the image should be retained
            when cropping.
        :param upscale: Should the image be enlarged if smaller than the dimensions?

        """
        self.width = width
        self.height = height
        self.anchor = anchor
        self.upscale = upscale

    def process(self, img):
        new_image = ResizeToCover(self.width, self.height,
                                  upscale=self.upscale).process(img)

        return new_image


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
        self.fields['price'].required = False

    price = forms.IntegerField(min_value=0, label='Цена', widget=forms.widgets.NumberInput(
        attrs={'placeholder': 'не больше', 'class': 'form-input'}))

    class Meta:
        model = InCityObject
        fields = ('sale_or_rent', 'object_type', 'price', 'city_region', 'rooms')


class OutCitySearchForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['city_distance'].empty_label = 'любая удаленность'
        self.fields['land_square'].required = False
        self.fields['city_distance'].required = False
        self.fields['object_type'].required = False
        self.fields['price'].required = False

    land_square = forms.IntegerField(min_value=0, label='Площадь участка', widget=forms.widgets.NumberInput(
        attrs={'placeholder': 'не менее (в сотках)', 'class': 'form-input'}))
    price = forms.IntegerField(min_value=0, label='Цена', widget=forms.widgets.NumberInput(
        attrs={'placeholder': 'не больше', 'class': 'form-input'}))

    class Meta:
        model = OutCityObject
        fields = ('object_type', 'price', 'city_distance', 'land_square')


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
                                processors=[ResizeToFill(1200, 800)],
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
    image = ProcessedImageField(spec_id='ecn:media:ecn_thumbnail',
                                label='Изменить изображение',
                                processors=[ResizeToFill(1200, 900)],
                                format='JPEG',
                                options={'quality': 70},
                                validators=[
                                    validators.FileExtensionValidator(allowed_extensions=('gif', 'jpg', 'png'))],
                                error_messages={'invalid_extension': 'Этот формат не поддерживается'},
                                widget=forms.widgets.FileInput)


class PhotoAddForm(forms.ModelForm):
    gallery_image = ProcessedImageField(spec_id='ecn:media:ecn_thumbnail',
                                        label='Изменить / добавить  изображение',
                                        processors=[ResizeToFill(1200, 900)],
                                        format='JPEG',
                                        options={'quality': 70},
                                        validators=[
                                            validators.FileExtensionValidator(
                                                allowed_extensions=('gif', 'jpg', 'jpeg', 'png'))],
                                        error_messages={'invalid_extension': 'Этот формат не поддерживается'},
                                        required=False,
                                        widget=forms.widgets.FileInput)

    is_published = forms.CharField(widget=forms.HiddenInput, label='', required=False, initial=True)
    note = forms.CharField(label='примечание (не обязательно)', required=False,
                           widget=forms.TextInput(attrs={'class': 'form-input'}), )


PhotoInlineFormSet = inlineformset_factory(
    InCityObject,
    Gallery,
    form=PhotoAddForm,
    fields='__all__',
    extra=9,
    max_num=10
)


class PhotoAddForm2(forms.ModelForm):
    gallery_image2 = ProcessedImageField(spec_id='ecn:media:ecn_thumbnail',
                                         label='Изменить / добавить  изображение',
                                         processors=[ResizeToFill(1200, 900)],
                                         format='JPEG',
                                         options={'quality': 70},
                                         validators=[
                                             validators.FileExtensionValidator(
                                                 allowed_extensions=('gif', 'jpg', 'jpeg', 'png'))],
                                         error_messages={'invalid_extension': 'Этот формат не поддерживается'},
                                         required=False,
                                         widget=forms.widgets.FileInput)

    is_published = forms.CharField(widget=forms.HiddenInput, label='', required=False, initial=True)
    note2 = forms.CharField(label='примечание (не обязательно)', required=False,
                            widget=forms.TextInput(attrs={'class': 'form-input'}), )


PhotoInlineFormSet2 = inlineformset_factory(
    OutCityObject,
    Gallery2,
    form=PhotoAddForm2,
    fields='__all__',
    extra=9,
    max_num=10
)
