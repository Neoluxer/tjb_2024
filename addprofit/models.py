from django.db import models


class AddProfits(models.Model):
    class Meta:
        verbose_name = "Поступления денежных средств"
        verbose_name_plural = "Доходы "

    description = models.TextField(verbose_name="description", null=True)
    price = models.FloatField(verbose_name="price", null=True)
    published = models.DateField(auto_now_add=True, db_index=True, verbose_name="published", null=True)
    category = models.IntegerField(verbose_name="category", null=True, default=0)
    id = models.AutoField(primary_key=True)
    customer = models.OneToOneField('Customer_category', null=True, on_delete=models.CASCADE, verbose_name='Заказчик',unique=True)


class Customer_category(models.Model):
    name = models.CharField(max_length=250, db_index=True, verbose_name='Заказчик',unique=True)
    id = models.AutoField(primary_key=True,db_index=True,verbose_name='id',unique=True)

    def __str__(self):
        result = f'{self.id}.   {self.name}'
        return result

    class Meta:
        verbose_name_plural = 'Заказчики'
        verbose_name = 'Заказчик'
        ordering = ['id']
