# Generated by Django 4.1.4 on 2023-04-05 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecn', '0002_alter_outcityobject_land_square_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incityobject',
            name='price',
            field=models.PositiveIntegerField(null=True, verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='outcityobject',
            name='price',
            field=models.PositiveIntegerField(null=True, verbose_name='Цена'),
        ),
    ]
