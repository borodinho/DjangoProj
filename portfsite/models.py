from django.contrib.auth.models import User
from django.db import models

# Create your models here.

# Создание модели, которая содержит в себе все главные аспекты по проектам

class ProjectItem(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100,verbose_name='Название проекта')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to='images',verbose_name='Изображение проекта')
    url = models.URLField(null=True, blank=True)

    STATUS =  [
        ('CRT', 'Текущий'),
        ('CMP', 'Завершен'),
    ]

    status = models.CharField(choices=STATUS, max_length=3, default='CMP', verbose_name='Статус проекта')

    def __str__(self):
        return self.title


class Comments(models.Model):
    user = models.ForeignKey(
        User,
        verbose_name="Пользователь",
        on_delete=models.CASCADE)
    new = models.ForeignKey(
         ProjectItem,
         verbose_name="Новость",
         on_delete=models.CASCADE)
    text = models.TextField("Комментарий")
    created = models.DateTimeField("Дата добавления", auto_now_add=True, null=True)
    moderation = models.BooleanField("Модерация", default=False)

