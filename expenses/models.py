from django.db import models


class AddExpenses(models.Model):
    class Meta:
        verbose_name = "Расход денежных средств"
        verbose_name_plural = "Расходы "

    description = models.TextField(verbose_name="description", null=True)
    price = models.FloatField(verbose_name="price", null=True)
    published = models.DateField(auto_now_add=True, db_index=True, verbose_name="published", null=True)
    category = models.IntegerField(verbose_name="category", null=True, default=0)
    id = models.AutoField(primary_key=True)



