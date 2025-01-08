from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        verbose_name='Пользователь',
        related_name='profile'
    )
    about = models.TextField(
        verbose_name='О себе',
        null=True,
        blank=True
    )
    image = models.ImageField(
        verbose_name='Аватар',
        upload_to='profiles/avatars/',
        null=True,
        blank=True
    )
    friends_qty = models.PositiveIntegerField(
        verbose_name='Кол-во друзей',
        default=0
    )
    streams_qty = models.PositiveIntegerField(
        verbose_name='Кол-во стримов',
        default=0
    )
    downloads_qty = models.PositiveIntegerField(
        verbose_name='Кол-во скачиваний игр',
        default=0
    )

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
