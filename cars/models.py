from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()



class Car(models.Model):
    '''Cars.'''
    vin = models.CharField(verbose_name='Вин', db_index=True, unique=True, max_length=64)
    color = models.CharField(verbose_name='цвет', max_length=64)
    brand = models.CharField(verbose_name='Бренд', max_length=64)
    CAR_TYPES = (
        (1, 'Универсал'),
        (2, 'Хатчбэк'),
        (3, 'Седан'),
        (4, 'Спортбек'),
        (5, 'Кабриолет'),
    )
    car_type = models.IntegerField(verbose_name='Вин', choices=CAR_TYPES)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)