# Generated by Django 4.1.5 on 2023-01-20 10:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecn', '0010_alter_contacts_image_alter_gallery_gallery_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incityobject',
            name='estate_agent',
            field=models.ForeignKey(default=1, help_text='специалист по объекту', on_delete=django.db.models.deletion.CASCADE, related_name='realtor', to=settings.AUTH_USER_MODEL, verbose_name='агент по недвижимости'),
        ),
    ]
