from django.db import models
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField
from django.urls import reverse


class User(AbstractUser):
    phone_number = models.CharField(max_length=12, blank=True, verbose_name='телефон для связи')

    def __str__(self):
        return self.username


# class Object(models.Model):
#     title = models.CharField(max_length=255, verbose_name='Заголовок')
#     slug = models.SlugField(unique=True, max_length=150, db_index=True, verbose_name='URL')
#     price = models.CharField(max_length=255, verbose_name='Цена')
#     image = models.ImageField(upload_to="images", blank=True, verbose_name='Основное изображение')
#     is_hot = models.BooleanField(default=False, verbose_name='горячий вариант', help_text='выделить объект')
#     object_adress = models.CharField(max_length=255, blank=True, verbose_name='адрес объекта',
#                                      help_text='необязательно')


