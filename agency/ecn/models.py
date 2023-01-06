from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    phone_number = models.CharField(max_length=12, blank=True, verbose_name='телефон для связи')

