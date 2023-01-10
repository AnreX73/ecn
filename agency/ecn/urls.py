from django.urls import path, include

from ecn.views import *

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
]

urlpatterns += [
    path('users/', include('django.contrib.auth.urls')),
    path('register/', Register.as_view(), name='register'),
    path('user_login/', UserLogin.as_view(), name='user_login'),
    path('user_password_reset/', UserPasswordReset.as_view(), name='user_password_reset'),
    path('user_password_reset_done/', UserPasswordResetDone.as_view(), name='user_password_reset_done'),
    path('profile/', profile, name='profile'),
   

]
