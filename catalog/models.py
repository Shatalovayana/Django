from django.db import models

from users.models import User

NULLABLE = {'null': True, 'blank': True}


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Категория товара')
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to='products/', **NULLABLE, verbose_name='Изображение')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    price = models.IntegerField(verbose_name='Цена за покупку')
    created_at = models.DateField(auto_now_add=True, verbose_name='Дата создания', **NULLABLE)
    date_of_last_changing = models.DateField(auto_now_add=True, verbose_name='Дата последнего изменения', **NULLABLE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь', **NULLABLE)
    is_published = models.BooleanField(default=False, verbose_name='Опубликовано')

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'
        permissions = [
            (
                'set_published',
                'Can publish posts'
            )
        ]


class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')
    version_number = models.IntegerField(verbose_name='Номер версии')
    version_title = models.CharField(max_length=150, verbose_name='Название версии')
    is_active = models.BooleanField(default=False, verbose_name='Признак текущей версии')

    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версии'
        get_latest_by = 'pk'

