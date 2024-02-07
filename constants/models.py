from django.db import models


class Constants(models.Model):
    class Meta:
        verbose_name = "Настройки telegram бота"
        verbose_name_plural = "Константы "


    description = models.TextField(verbose_name="description", null=True)
    key = models.CharField(max_length=50, db_index=True, verbose_name='key')
    value = models.CharField(max_length=50, db_index=True, verbose_name='value')
