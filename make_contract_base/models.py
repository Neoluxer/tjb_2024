from datetime import datetime

from django.db import models

dt = datetime.utcnow()


class ContractBase(models.Model):
    class Meta:
        verbose_name = "Договор с юр.лицом"
        verbose_name_plural = "Договора"

    contract_file = models.FileField(upload_to='files/', default='DEFAULT VALUE', verbose_name='Путь к файлу',
                                     null=True)
    customer_delegate = models.CharField(verbose_name="ФИО представителя", null=True,
                                         default="Иванов Иван Иванович")
    quantity = models.IntegerField(verbose_name="Количество", null=True, default=50)
    prefix = models.DateTimeField(db_index=True, verbose_name="prefix", null=True)
    number = models.AutoField(primary_key=True, verbose_name="Номер договора")
    price = models.FloatField(verbose_name="цена за еденицу", null=True, default=100)
    date = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name="date", null=True)
    mail = models.EmailField(verbose_name="email", null=True, default="neoluxe@yandex.ru")
    total_cost = models.FloatField(verbose_name="Общая сумма договора", null=True, default=10000)
    adressofobject = models.CharField(verbose_name="Адрес объекта", null=True,
                                      default="350010,г. Краснодар, ул. Зиповская, д. 5 Литера Х, офис 28")
    townobject = models.CharField(verbose_name="Город", null=True, default="Москва")
    telephonenum = models.CharField(verbose_name="телефон", null=True, default="+79780740854")
    customer_firm = models.CharField(verbose_name="Название организации", null=True,
                                     default="ООО 'Рога и копыта' ")
    organization_full_name = models.CharField(verbose_name="Полное наименование", null=True,
                                              default="Общество с ограниченной ответственностью 'Рога и копыта'")
    organization_adress = models.CharField(verbose_name="Адрес организации", null=True,
                                           default="г. Краснодар")
    customer_legal_basis = models.CharField(verbose_name="Основание", null=True,
                                            default="Устава предприятия")
    organization_inn = models.BigIntegerField(verbose_name="ИНН", null=True, default=6658215373)
    organization_kpp = models.BigIntegerField(verbose_name="КПП", null=True, default=23100100)
    ogrn = models.BigIntegerField(verbose_name="ОГРН", null=True, default=1026605606620)
    date_of_firm_registration = models.DateTimeField(verbose_name="дата регистрации", null=True)
    okpo = models.BigIntegerField(verbose_name="ОКПО", null=True, default=8729037291)
    organization_rs = models.CharField(verbose_name="Р/С", null=True, default='12345678912345678912')
    bank_name = models.CharField(max_length=250, verbose_name="Название банка", null=True, default="ПАО КБ УБРИР")
    bank_bik = models.CharField(verbose_name="БИК", null=True,
                                default="046577795")  # Поменять в handler и Class
    bank_ks = models.CharField(verbose_name="К/С", null=True, default='30101810900000000795')
    customer = models.ForeignKey('Organization', null=True, on_delete=models.PROTECT, verbose_name='Организация')

    def __str__(self):
        return str(self.number)


class Organization(models.Model):
    name = models.CharField(max_length=250, db_index=True, verbose_name='Заказчик')
    id = models.AutoField(primary_key=True)

    customer_delegate = models.CharField(max_length=255, verbose_name="ФИО представителя", null=True,
                                         default="Иванов Иван Иванович")
    mail = models.EmailField(verbose_name="email", null=True, default="neoluxe@yandex.ru")
    telephonenum = models.CharField(max_length=25, verbose_name="телефон", null=True, default="+79780740854")
    organization_full_name = models.CharField(max_length=100, verbose_name="Полное наименование", null=True,
                                              default="Общество с ограниченной ответственностью 'Рога и копыта'")
    organization_adress = models.CharField(max_length=250, verbose_name="Адрес организации", null=True,
                                           default="Общество с ограниченной ответственностью 'Рога и копыта'")
    organization_inn = models.BigIntegerField(verbose_name="ИНН", null=True, default=6658215373)
    organization_kpp = models.BigIntegerField(verbose_name="КПП", null=True, default=23100100)
    ogrn = models.BigIntegerField(verbose_name="ОГРН", null=True, default=1026605606620)
    okpo = models.CharField(max_length=250, verbose_name="ОКПО", null=True, default=8729037291)
    organization_rs = models.CharField(max_length=250, verbose_name="Р/С", null=True, default='12345678912345678912')
    bank_name = models.CharField(max_length=25, verbose_name="Название банка", null=True, default="ПАО КБ УБРИР")
    bank_bik = models.CharField(max_length=25, verbose_name="БИК", null=True, default="046577795")
    bank_ks = models.CharField(max_length=250, verbose_name="К/С", null=True, default='30101810900000000795')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Организации'
        verbose_name = 'Организация'
        ordering = ['name']


class PrivateContract(models.Model):
    class Meta:
        verbose_name = "Договор физ.лицо"
        verbose_name_plural = "Договора с физ.лицами "

    customername = models.ForeignKey('addprofit.Customer_category', on_delete=models.PROTECT, null=True,
                                     verbose_name='Заказчик', default='null')
    private_contract_file = models.FileField(upload_to='files/', default='DEFAULT VALUE',
                                             verbose_name='Путь к файлу (Договор)',
                                             null=True)
    quantity = models.IntegerField(verbose_name='Количество', null=True, default=0)
    source = models.CharField(max_length=300, verbose_name='Предмет договора', null=True, default='дизайн проект')
    price = models.IntegerField(verbose_name='Цена', null=True, default=0)
    square = models.IntegerField(verbose_name='Площадь', null=True, default=0)
    address_of_object = models.CharField(verbose_name='Адрес объекта', null=True, default='null')
    town_object = models.CharField(verbose_name='Город', null=True, default='null')
    id = models.AutoField(primary_key=True)
    published = models.DateField(db_index=True, verbose_name="Дата", null=True)

    def __str__(self):
        result = "Договор №" + str(self.id) + "_" + str(self.address_of_object) + "_" + str(
            int(self.price) * int(self.square)) + "_" + str(self.source) + "_" + str(self.customername) + "_" + str(
            self.published)
        return result
