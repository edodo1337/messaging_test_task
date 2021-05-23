from django.db import models

from messaging import mixins


class Message(models.Model):
    title = models.CharField(
        verbose_name="Заголовок",
        max_length=255, blank=False, null=False
    )

    body = models.TextField(
        verbose_name="Тело сообщения", blank=False, null=False
    )

    flag_sent = models.BooleanField(
        verbose_name="Флаг отправки", default=False
    )

    flag_read = models.BooleanField(
        verbose_name="Флаг прочтения", default=False
    )

    user = models.ForeignKey(
        'users.User',
        verbose_name='Пользователь',
        related_name='messages',
        on_delete=models.SET_NULL,
        null=True
    )

    created_at = models.DateTimeField(verbose_name="Создан", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Обновлен", auto_now=True)

    class Meta:
        ordering = ['created_at']
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
        ordering = ('created_at',)

    def __repr__(self) -> str:
        return f'<Message: {self.title} / {self.created_at} / {self.updated_at}'
    
    def __str__(self) -> str:
        return f'Сообщение: {self.title} от {str(self.user)}'

    def mark_read(self):
        self.flag_read = True
        self.save()