from django.db import models


class Category(models.Model):
    name = models.CharField(
        verbose_name='Категория',
        max_length=128,
        unique=True
    )
    slug = models.SlugField(
        max_length=32,
        unique=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name']


class Genre(models.Model):
    name = models.CharField(
        verbose_name='Жанр',
        max_length=128,
        unique=True
    )
    slug = models.SlugField(
        max_length=32,
        unique=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'
        ordering = ['name']


class Title(models.Model):
    name = models.CharField(
        verbose_name='Наименование',
        max_length=128
    )
    genre = models.ManyToManyField(
        Genre,
        verbose_name='Жанр',
        related_name='titles',
        blank=True

    )
    category = models.ForeignKey(
        Category,
        verbose_name='Категория',
        on_delete=models.SET_NULL,
        related_name='titles',
        blank=True,
        null=True
    )
    year = models.IntegerField(
        verbose_name='Дата выхода',
        db_index=True,
        null=True,
    )
    description = models.CharField(
        verbose_name='Описание',
        max_length=256,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Произведение'
        verbose_name_plural = 'Произведения'
        ordering = ['name']


