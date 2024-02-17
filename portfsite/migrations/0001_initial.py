# Generated by Django 4.2.9 on 2024-01-14 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название проекта')),
                ('description', models.TextField(verbose_name='Описание')),
                ('image', models.ImageField(upload_to='images', verbose_name='Изображение проекта')),
                ('status', models.CharField(choices=[('CRT', 'Текущий'), ('CMP', 'Завершен')], default='CMP', max_length=3, verbose_name='Статус проекта')),
            ],
        ),
    ]
