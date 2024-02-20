from django.db import models


# Create your models here.
class Offer(models.Model):
    class Meta:
        verbose_name = "КП"
        verbose_name_plural = "Коммерческие предложения "

    offer_file = models.FileField(upload_to='files/', default='DEFAULT VALUE', verbose_name='Путь к файлу (КП)',
                                    null=True)
    title = models.CharField(verbose_name="Заголовок", max_length=255)  # Имя
    town = models.CharField(verbose_name="Город", max_length=255)  # Город
    offer_number = models.CharField(max_length=50, verbose_name="Номер КП", null=True, default='null')
    value = models.IntegerField(verbose_name="Итоговая стоимость с учётом скидки", null=True,
                                default=0)  # Сумма покупки?
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name="Дата создания КП", null=True)
    id = models.AutoField(primary_key=True)
    area = models.IntegerField()
    address = models.CharField(max_length=250, verbose_name='Адрес', null=True, )
    ruberic = models.ForeignKey('make_contract_base.ContractBase', on_delete=models.PROTECT, null=True,
                                verbose_name='Номер договора')
    customer = models.ForeignKey('addprofit.Customer_category', on_delete=models.PROTECT, null=True,
                                 verbose_name='Заказчик')

    project_choices = [("F", "планировка"),
                       ("DP", "обмерный план"),
                       ("M", "обмеры"),
                       ("V", "визуализация"),
                       ("FDP", "полный дизайн проект"),
                       ("FP", "фор-проект"),
                       ("CDP", "проект с комплектацией"),
                       ("ADP", "проект с авторским надзором")
                       ]

    project_composition = models.CharField(max_length=3, choices=project_choices, default="F")

    def __str__(self):
        return str(self.title)+" № "+str(self.id)+" - "+str(self.customer)+" - "+str(self.published)
# Адрес (есть)
# Город (есть)
# Номер КП (есть)
# Ссылка на договор (есть)
# Ссылка на счет (не нужно)
# Ссылка на заказчика (есть)
# Площадь (есть)
# Дата создания КП (есть)
# Заголовок (есть)
# Итоговая стоимость с учётом скидки (1,2,3) (есть)


# Состав проекта (Вариант 1,2,3)
# Сроки выполнения проекта
# Стоимость для вариантов (1,2,3)
# Скидка
# Первый платёж
# Второй платёж
# Третий платёж
# Четвертый платёж
