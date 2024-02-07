from django.db import models


class Invoice(models.Model):
    class Meta:
        verbose_name = "Счёт"
        verbose_name_plural = "Счета "

    id = models.AutoField(primary_key=True)
    invoice_file = models.FileField(upload_to='files/', default='DEFAULT VALUE', verbose_name='Путь к файлу (акт)',
                                     null=True)
    invoice_file_invoice = models.FileField(upload_to='files/', default='DEFAULT VALUE', verbose_name='Путь к файлу (счёт)',
                                    null=True)
    name = models.CharField(verbose_name="Основание платежа", max_length=255, null=True)  # Имя
    published = models.DateField(db_index=True, verbose_name="Дата", null=True)
    sum = models.IntegerField(verbose_name="Сумма", null=True)
    invoice_number = models.CharField(max_length=50, verbose_name="Номер счета", null=True, default='null')
    ruberic = models.ForeignKey('make_contract_base.ContractBase', on_delete=models.PROTECT, null=True,
                                verbose_name='Номер договора')
    customer = models.ForeignKey('addprofit.Customer_category', on_delete=models.PROTECT, null=True,
                                 verbose_name='Заказчик')
    organisation = models.ForeignKey('make_contract_base.Organization', on_delete=models.PROTECT, null=True,
                                 verbose_name='Организация')
