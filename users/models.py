from pyexpat import model
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    image = models.ImageField(upload_to='users_images', blank=True, null=True, verbose_name='Аватар')
    is_seller = models.BooleanField(verbose_name='Продавец', default=False)
    role = models.CharField(verbose_name='Роль', max_length=100, default='customer')

    class Meta:
        # Имя SQL-таблицы
        db_table = 'user'
        # Как отображается в Админ-панели
        verbose_name = 'Пользователя'
        verbose_name_plural = 'Пользователи'


    def __str__(self):
        return f'{self.username}'
