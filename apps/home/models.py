

from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Genre(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name='Название жанра'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'


class UserClip(models.Model):
    name = models.CharField(
        verbose_name='Название',
        max_length=100
    )
    views = models.PositiveIntegerField(
        verbose_name='Кол-во просмотров',
        default=0
    )
    url = models.URLField(
        verbose_name='Ссылка на клип'
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Пользователь',
        related_name='clips'
    )
    preview = models.ImageField(
        verbose_name='Превью',
        upload_to='clips/previews/',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Клип пользователя'
        verbose_name_plural = 'Клипы пользователей'


class Game(models.Model):
    name = models.CharField(
        verbose_name='Название',
        max_length=100
    )
    genre = models.ForeignKey(
        Genre,
        on_delete=models.CASCADE,
        verbose_name='Жанр',
        related_name='genres'
    )
    preview = models.ImageField(
        verbose_name='Превью',
        upload_to='games/previews/',
        blank=True,
        null=True
    )
    added_at = models.DateTimeField(
        verbose_name='Дата добавления',
        auto_now_add=True
    )
    trailer = models.URLField(
        verbose_name='Ссылка на трейлер',
        null=True,
        blank=True
    )
    sub_genre = models.CharField(
        verbose_name='Поджанр',
        max_length=100,
        blank=True,
        null=True
    )
    description = models.TextField(
        verbose_name='Описание',
        null=True,
        blank=True
    )
    downloads = models.PositiveIntegerField(
        verbose_name='Кол-во скачиваний',
        default=0
    )
    size = models.FloatField(
        verbose_name='Размер',
        default=0.0
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Игра'
        verbose_name_plural = 'Игры'


class GameImage(models.Model):
    game = models.ForeignKey(
        Game,
        on_delete=models.CASCADE,
        related_name='images',
        verbose_name='Игра',
    )
    image = models.ImageField(
        upload_to='games/images/',
        null=True,
        blank=True,
        verbose_name='Фото'
    )


class Stream(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name='Название'
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Пользователь',
        related_name='streams'
    )
    game = models.ForeignKey(
        Game,
        on_delete=models.CASCADE,
        verbose_name='Игра',
        related_name='streams'
    )
    preview = models.ImageField(
        upload_to='previews/streams',
        verbose_name='Превью',
        null=True,
        blank=True
    )
    viewers = models.PositiveIntegerField(
        default=0,
        verbose_name='Кол-во зрителей'
    )
    is_live = models.BooleanField(
        default=False,
        verbose_name='Онлайн'
    )
    started_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата старта'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Стрим'
        verbose_name_plural = 'Стримы'

# user
# request.user
# request.user.library

class Library(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='library',
                             verbose_name='Пользователь')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Библиотека пользователя: {self.user.username}'

    class Meta:
        verbose_name = 'Библиотека пользователя'
        verbose_name_plural = 'Библиотеки пользователей'
        ordering = ['-created_at']


class LibraryItem(models.Model):
    library = models.ForeignKey(Library, on_delete=models.CASCADE,
                                related_name='library_items', verbose_name='Библиотека')
    game = models.ForeignKey(Game, on_delete=models.CASCADE, verbose_name='Игра')
    is_downloaded = models.BooleanField(default=False, verbose_name='Статус')
    created_at = models.DateTimeField(auto_now_add=True)  # при создании добавляется время
    updated_at = models.DateTimeField(auto_now=True)  # время меняется при изменении элемента

    def __str__(self):
        return self.game.name

    class Meta:
        verbose_name = 'Игра в библиотеке'
        verbose_name_plural = 'Игры в библиотеке'
        ordering = ['-updated_at']


