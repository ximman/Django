from PIL import Image
from django.db import models
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey
from imagekit.models.fields import ImageSpecField
from imagekit.processors import ResizeToFit
from pilkit.processors import Adjust


class Product(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Цена')
    photo = models.ImageField(
        upload_to = 'photos/%Y/%m/%d/',
        verbose_name='Фото',
        null=True,
        blank=True
    )
    photo_s = ImageSpecField(
        [Adjust(contrast=1.2, sharpness=1.1),
         ResizeToFit(50,50)],
        source='photo',
        format='JPEG',
        options={'quality':90}
    )
    photo_m = ImageSpecField(
        [Adjust(contrast=1.2, sharpness=1.1),
         ResizeToFit(300, 200)],
        source='photo',
        format='JPEG',
        options={'quality': 90}
    )
    photo_l = ImageSpecField(
        [Adjust(contrast=1.2, sharpness=1.1),
         ResizeToFit(640, 480)],
        source='photo',
        format='JPEG',
        options={'quality': 90}
    )
    cat = models.ForeignKey('Category', on_delete = models.PROTECT, verbose_name='Категория')
    subcat = TreeForeignKey('Subcategory', on_delete=models.PROTECT, verbose_name='Подкатегория')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product', kwargs = {'product_slug' : self.slug})

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['id']

class Category(MPTTModel):
    name = models.CharField(max_length = 100, db_index = True, verbose_name='Категория')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    photo = models.ImageField(
        upload_to='photos/%Y/%m/%d/',
        verbose_name='Фото',
        null=True,
        blank=True
    )
    parent = TreeForeignKey(
        'self',
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        db_index=True,
        related_name='parents',
        verbose_name='Пока не знаю')
    # level = models.PositiveIntegerField(default=0)
    # lft = models.PositiveIntegerField(default=0)
    # rght = models.PositiveIntegerField(default=1)
    # tree_id = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs = {'cat_slug' : self.slug})

    # class MPTTMeta:
    #     order_insertion_by = ['name']

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['id']

class Subcategory(MPTTModel):
    name = models.CharField(max_length = 100, db_index = True, verbose_name='Подкатегория')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    photo = models.ImageField(
        upload_to='photos/%Y/%m/%d/',
        verbose_name='Фото',
        null=True,
        blank=True
    )
    parent = TreeForeignKey(
        'Category',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children',
        db_index=True,
        verbose_name='Родительская категория')
    # level = models.PositiveIntegerField(default=1)
    # lft = models.PositiveIntegerField(default=0)
    # rght = models.PositiveIntegerField(default=2)
    # tree_id = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('subcategory', kwargs = {'subcat_slug' : self.slug})

    class Meta:
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'
        ordering = ['id']

    class MPTTMeta:
        order_insertion_by = ['name']