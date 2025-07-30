from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class TodoModel(models.Model):
    STATUS_DICT = [
        ('new', 'Новый'),
        ('in_progress', 'В исполнении'),
        ('done', 'Выполнено')
    ]
    title = models.CharField(verbose_name='Задача')
    term = models.DateTimeField(null=True, blank=True, verbose_name='Срок')
    creating_date = models.DateTimeField(verbose_name='Создана', auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True, verbose_name='Отредактировно')
    priority = models.IntegerField(verbose_name='Приоритет')
    status = models.CharField(choices=STATUS_DICT, verbose_name='Статус')
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    