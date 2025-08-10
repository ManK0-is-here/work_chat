from django.db import models


class Problems(models.Model):

    def __str__(self):
        return "Ты это написал"

    STATUS_PROBLEM = [
        ('not accepted', 'Ожидает'),
        ('at work','В работе'),
        ('completed','Готова'),
        ('cancelled', 'Отменена')
    ]

    name_problem = models.CharField(max_length=200, verbose_name="Задача")

    mess_problem = models.TextField(blank=True, null=True, verbose_name="Комментарий")

    date_create = models.DateTimeField(verbose_name="Дата создания")

    deadlines = models.DateTimeField(null=True, blank=True, default="Не срочное", verbose_name="Крайний срок")

    status = models.CharField(choices=STATUS_PROBLEM, verbose_name="Статус")

    value = models.IntegerField(max_value=100, min_value=1, verbose_name="Очки за выполнение")

    class Meta:
        verbose_name = "Задача"
        verbose_name_plural="Задачи"


