# Generated by Django 4.1.4 on 2023-01-26 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecn', '0012_alter_incityobject_estate_agent_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.CharField(blank=True, max_length=30, verbose_name='телефон для связи'),
        ),
    ]
