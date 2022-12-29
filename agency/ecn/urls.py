from django.urls import path

from ecn.views import *

urlpatterns = [
    path('', index, name='home'),


]
