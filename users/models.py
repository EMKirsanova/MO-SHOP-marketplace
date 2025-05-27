from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    image = models.ImageField(upload_to='users_images', blank=True, null=True, verbose_name='Аватар')
    phone_number = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        # Имя SQL-таблицы
        db_table = 'user'
        # Как отображается в Админ-панели
        verbose_name = 'Пользователя'
        verbose_name_plural = 'Пользователи'


    def __str__(self):
        return f'{self.username}'
