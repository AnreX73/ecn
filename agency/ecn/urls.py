from django.urls import path, include

from ecn.views import *

urlpatterns = [
    path('', index, name='home'),
    path('searched_obj/', searched_obj, name='searched_obj'),
    path('show_apartments/<slug:obj_type_slug>', show_apartments, name='show_apartments'),
    path('show_dachas/<slug:obj_type_slug>', show_dachas, name='show_dachas'),
    path('show_rent/<slug:obj_type_slug>', show_rent, name='show_rent'),
    path('show_apartment/<slug:apartment_slug>', show_apartment, name='show_apartment'),
    path('show_dacha/<slug:dacha_slug>', show_dacha, name='show_dacha'),

]

urlpatterns += [
    path('users/', include('django.contrib.auth.urls')),
    path('register/', Register.as_view(), name='register'),
    path('user_login/', UserLogin.as_view(), name='user_login'),
    path('user_password_reset/', UserPasswordReset.as_view(), name='user_password_reset'),
    path('user_password_reset_done/', UserPasswordResetDone.as_view(), name='user_password_reset_done'),
    path('profile/<slug:slug>/', ObjectUpdateView.as_view(), name='object_edit'),
    path('profile/<slug:slug>/delete/', ObjectDeleteView.as_view(), name='object_delete'),
    path('profile/', profile, name='profile'),
    path('add_object/', add_object, name='add_object'),
    path('update_user_info/', UpdateUserInfo.as_view(), name='update_user_info'),
   

]
