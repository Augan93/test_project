from django.db import models
from common.models import BaseModel
from django.contrib.auth import get_user_model

User = get_user_model()


def get_sentinel_user():
    return User.objects.get_or_create(username='deleted')[0]


class Car(BaseModel):
    owner = models.ForeignKey(
        User,
        on_delete=models.SET(get_user_model),
        related_name='my_cars',
        verbose_name='Хозяин',
    )
    car_id = models.AutoField(
        primary_key=True,
    )
    color = models.CharField(
        max_length=100,
        verbose_name='Цвет',
    )
    year = models.PositiveIntegerField(
        verbose_name='Год',
    )
    manufacturer = models.CharField(
        max_length=200,
        verbose_name='Произваодитель',
    )

    def __str__(self):
        return '{} - {}'.format(self.color,
                                self.car_id)

    class Meta:
        verbose_name = 'Автомобиль'
        verbose_name_plural = 'Автомобили'


