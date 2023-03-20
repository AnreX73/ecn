# Generated by Django 4.1.4 on 2023-03-22 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecn', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='outcityobject',
            name='land_square',
            field=models.PositiveIntegerField(blank=True, verbose_name='площадь участка'),
        ),
        migrations.AlterField(
            model_name='roomamount',
            name='room_amount',
            field=models.PositiveIntegerField(unique=True, verbose_name='Кол-во комнат цифрами'),
        ),
        migrations.AlterField(
            model_name='roomamount',
            name='slug',
            field=models.SlugField(max_length=150, verbose_name='URL'),
        ),
    ]