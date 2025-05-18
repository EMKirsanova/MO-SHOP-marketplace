from statistics import quantiles
from tabnanny import verbose
from django.db import models


# Create your models here.
class Categories(models.Model):
    # поле id создаётся для каждого класса автоматически (settings.py/DEFAULT_AUTO_FIELD)
    # имя категории
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    # фрагмент текстового url-адреса, который будет вести на категорию
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')

    class Meta:
        # Имя SQL-таблицы
        db_table = 'category'
        # Как отображается в Админ-панели
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'
    

    def __str__(self):
        return self.name


class Products(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    image = models.ImageField(upload_to='goods_images', blank=True, null=True, verbose_name='Изображение')
    price = models.DecimalField(default=0.00, max_digits=7, decimal_places=2, verbose_name='Цена')
    discount = models.DecimalField(default=0.00, max_digits=4, decimal_places=2, verbose_name='Скидка в %')
    quantity = models.PositiveIntegerField(default=0, verbose_name='Количество')
    # PROTECT: если категорию удаляют, а к ней еще привязаны товары, то удаление запрещается
    # CASCADE: если категорию удаляют, а к ней еще привязаны товары, то все они тоже удаляются (после предупреждения об этом)
    category = models.ForeignKey(to=Categories, on_delete=models.CASCADE, verbose_name='Категория')


    class Meta:
        # Имя SQL-таблицы
        db_table = 'product'
        # Как отображается в Админ-панели
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


    def __str__(self):
        return f'{self.name} | Количество: {self.quantity}'

# для создания fixtures в UTF-8:
# python -Xutf8 manage.py dumpdata goods.Products > fixtures/goods/prod.json
