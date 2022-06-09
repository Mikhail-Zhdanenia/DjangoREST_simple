# Generated by Django 4.0.5 on 2022-06-08 08:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vin', models.CharField(db_index=True, max_length=64, verbose_name='Вин')),
                ('color', models.CharField(max_length=64, verbose_name='цвет')),
                ('brand', models.CharField(max_length=64, verbose_name='Бренд')),
                ('car_type', models.IntegerField(choices=[(1, 'Универсал'), (2, 'Хатчбэк'), (3, 'Седан'), (4, 'Спортбек'), (5, 'Кабриолет')], verbose_name='Вин')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
        ),
    ]