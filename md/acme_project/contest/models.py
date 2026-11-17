from django.db import models


class Contest(models.Model):
    title = models.CharField(max_length=20, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    price = models.IntegerField(verbose_name='Цена')
    comment = models.TextField(blank=True, verbose_name='Комментарий')

    def __str__(self):
        return self.title