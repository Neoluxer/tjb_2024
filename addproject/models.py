from django.db import models




class Project(models.Model):
    class Meta:
        verbose_name = "Объект"
        verbose_name_plural = "Дизайн проект"


    year = models.IntegerField()
    name = models.CharField(max_length=250, verbose_name='Название проекта', null=True, )
    area = models.IntegerField()
    address = models.CharField(max_length=250, verbose_name='Адрес', null=True, )

    id = models.AutoField(primary_key=True)
    published = models.DateTimeField(db_index=True, verbose_name='Дата', null=True)
    ruberic = models.ForeignKey('make_contract_base.ContractBase',on_delete=models.PROTECT, null=True, verbose_name='Номер договора')

