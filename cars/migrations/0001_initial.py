# Generated by Django 2.1.7 on 2019-05-03 14:51

from django.conf import settings
import django.contrib.auth
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('is_active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('deleted', models.DateTimeField(blank=True, null=True)),
                ('car_id', models.AutoField(primary_key=True, serialize=False)),
                ('color', models.CharField(max_length=100, verbose_name='Цвет')),
                ('year', models.PositiveIntegerField(verbose_name='Год')),
                ('manufacturer', models.CharField(max_length=200, verbose_name='Произваодитель')),
                ('owner', models.ForeignKey(on_delete=models.SET(django.contrib.auth.get_user_model), related_name='my_cars', to=settings.AUTH_USER_MODEL, verbose_name='Хозяин')),
            ],
            options={
                'verbose_name': 'Автомобиль',
                'verbose_name_plural': 'Автомобили',
            },
        ),
    ]
