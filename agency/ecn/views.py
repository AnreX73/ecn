from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordResetDoneView
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from ecn.models import *
from ecn.slugify import words_to_slug

from ecn.forms import UserCreationForm, UserLoginForm, UserPasswordResetForm, InCitySearchForm, InCityAddForm, \
    ChangeUserlnfoForm, InCityUpdateForm


def index(request):
    context = {
        'title': 'Агенство ЕЦН',
        'main_page_img': Graphics.objects.get(description='изображение на главную'),
        'main_page_slogan': Graphics.objects.get(description='Слоган'),
        'hot_city_obj': InCityObject.objects.filter(is_hot=True).filter(sale_or_rent='s').order_by('-time_create'),
        'hot_out_city_obj': OutCityObject.objects.filter(is_hot=True).order_by('-time_create'),
        'hot_title': Graphics.objects.get(description='горячая кнопка на главной'),
        'no_photo': Graphics.objects.get(description='нет фото'),
        'services': Post.objects.all(),
    }
    return render(request, 'ecn/index.html', context=context)


def show_apartments(request, obj_type_slug):
    apartments_type = get_object_or_404(InCityObjectType, slug=obj_type_slug)
    unselected_links = InCityObjectType.objects.exclude(slug=obj_type_slug)

    context = {
        'apartments_type': apartments_type,
        'unselected_links': unselected_links,
        'search_icon': Graphics.objects.get(description='иконка поиска'),

    }
    return render(request, 'ecn/show_apartments.html', context=context)


def show_dachas(request, obj_type_slug):
    dachas_type = get_object_or_404(OutCityObjectType, slug=obj_type_slug)
    unselected_links = OutCityObjectType.objects.exclude(slug=obj_type_slug)
    context = {
        'dachas_type': dachas_type,
        'unselected_links': unselected_links,

    }
    return render(request, 'ecn/show_dachas.html', context=context)


def show_rent(request, obj_type_slug):
    rent_obj_type = get_object_or_404(InCityObjectType, slug=obj_type_slug)
    unselected_links = InCityObjectType.objects.exclude(slug=obj_type_slug)
    context = {
        'rent_obj_type': rent_obj_type,
        'unselected_links': unselected_links,

    }
    return render(request, 'ecn/show_rent.html', context=context)


def show_apartment(request, apartment_slug):
    apartment = get_object_or_404(InCityObject, slug=apartment_slug)
    apartment_id = apartment.id
    context = {
        'apartment': apartment,
        'gallery': Gallery.objects.filter(galleryLink_id=apartment_id),
        'no_photo': Graphics.objects.get(description='нет фото')
    }
    return render(request, 'ecn/apartment.html', context=context)


def show_dacha(request, dacha_slug):
    dacha = get_object_or_404(OutCityObject, slug=dacha_slug)
    dacha_id = dacha.id
    context = {
        'dacha': dacha,
        'gallery': Gallery2.objects.filter(galleryLink2_id=dacha_id),
        'no_photo': Graphics.objects.get(description='нет фото')
    }
    return render(request, 'ecn/dacha.html', context=context)


def searched_obj(request):
    if request.method == 'POST':
        form = InCitySearchForm(request.POST)
        if form.is_valid():
            obj_dic = {k: v for k, v in form.cleaned_data.items() if v is not None}
            selected_items = InCityObject.objects.filter(**obj_dic).filter(is_published=True)

    else:
        selected_items = InCityObject.objects.filter(sale_or_rent='s')
        form = InCitySearchForm()
    context = {
        'title': 'Агенство ЕЦН - поиск',
        'form': form,
        'selected_items': selected_items,
        'no_photo': Graphics.objects.get(description='нет фото'),

    }
    return render(request, 'ecn/searched_obj.html', context=context)


@login_required(login_url='/register/')
def profile(request):
    user_good = request.user
    context = {
        'title': 'Your page',
        'user': user_good.first_name,
        'user_nick': user_good.username,
        'date_joined': user_good.date_joined,
        'user_phone': user_good.phone_number,
        'user_email': user_good.email,
        'user_in': user_good.is_authenticated,
        'user_city_objects': InCityObject.objects.filter(estate_agent__id=user_good.id),
        'user_out_city_objects': OutCityObject.objects.filter(estate_agent__id=user_good.id)

    }
    return render(request, 'registration/profile.html', context=context)


class Register(View):
    template_name = 'registration/register.html'

    def get(self, request):
        context = {
            'form': UserCreationForm(),
            'title': 'регистрация',
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('profile')
        context = {
            'form': form,
        }
        return render(request, self.template_name, context)


class UserLogin(SuccessMessageMixin, LoginView):
    template_name = 'registration/user_login.html'
    form_class = UserLoginForm
    success_message = 'Вы авторизованы!'


class UserPasswordReset(PasswordResetView):
    template_name = 'registration/user_password_reset.html'
    form_class = UserPasswordResetForm

    def get_success_url(self):
        return reverse_lazy('user_password_reset_done')


class UserPasswordResetDone(PasswordResetDoneView):
    template_name = 'registration/user_password_reset_done.html'


@login_required(login_url='/register/')
def add_object(request):
    if request.method == 'POST':
        form = InCityAddForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            new_slug = words_to_slug(title)
            comment = form.save(commit=False)
            comment.is_published = True
            comment.slug = new_slug
            comment.is_hot = True
            comment.save()

            return redirect('profile')

    else:
        form = InCityAddForm(initial=dict(estate_agent=request.user))

    context = {
        'form': form,
    }

    return render(request, 'registration/add_object.html', context=context)


class UpdateUserInfo(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = User
    template_name = 'registration/update_user_info.html'
    form_class = ChangeUserlnfoForm
    success_url = reverse_lazy('profile')
    success_message = 'Данные пользователя изменены'

    def setup(self, request, *args, **kwargs):
        self.user_id = request.user.pk
        return super().setup(request, *args, **kwargs)

    def get_object(self, queryset=None):
        if not queryset:
            queryset = self.get_queryset()
        return get_object_or_404(queryset, pk=self.user_id)


class ObjectUpdateView(LoginRequiredMixin, UpdateView):  # Новый класс
    model = InCityObject
    template_name = 'registration/update_object.html'
    form_class = InCityUpdateForm

   
