from django.contrib.auth.models import AbstractUser
from django.db import models
from users.manager import CustomUserManager


class User(AbstractUser):
    ip = models.CharField(verbose_name='IP адрес', max_length=25, blank=False)
    
    banned_at = models.DateTimeField(verbose_name='Время последнего бана', null=True)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'    
    
    def __repr__(self) -> str:
        return f'<User: {self.username}'
    
    def __str__(self) -> str:
        return f'Пользователь: {self.username}'