from django.db import models

# Create your models here.

from django.contrib.auth.models import User


class Note(models.Model):
    # Модель записки
    
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    title = models.CharField('Заголовок', max_length=30)
    text = models.CharField('Текст', max_length=250)
    creation_date = models.DateTimeField('Дата создания', auto_now_add=True)
    modify_date = models.DateTimeField('Дата изменения', auto_now=True)

    class Meta:
        ordering = ['creation_date']

    def __str__(self):
        return self.title