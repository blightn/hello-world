from django.db import models

# Create your models here.

class FirstApp(models.Model):
    """ Модель записи """
    
    title = models.CharField('Заголовок', max_length=50)
    description = models.CharField('Описание', max_length=250)
    date = models.DateTimeField('Дата', auto_now_add=True)

    def __str__(self):
        return self.title