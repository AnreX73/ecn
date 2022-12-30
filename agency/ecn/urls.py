from django.urls import path, include

from ecn.views import *

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
]

urlpatterns += [
    path('users/', include('django.contrib.auth.urls')),
    path('register/', Register.as_view(), name='register'),

]
