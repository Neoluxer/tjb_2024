from django.db import models


# Create your models here.
class Customers(models.Model):
    class Meta:
        verbose_name = "Клиент дизайн студии"
        verbose_name_plural = "Заказчики "

    name = models.CharField(verbose_name="Имя", max_length=255)  # Имя
    ln = models.CharField(max_length=255, verbose_name="Отчество", null=True, default='null')  # Отчество
    fn = models.CharField(max_length=255, verbose_name="Фамилия", null=True, default='null')  # Фамилия
    gen = models.CharField(max_length=255, verbose_name="Гендер", null=True, default='f')  # Гендер
    age = models.IntegerField(verbose_name="Возраст", null=True, default=0)  # Возраст
    dob = models.DateField(verbose_name="Дата Рождения", null=True, default='29.11.2023')  # db дата рождения
    doby = models.CharField(max_length=255, verbose_name="Год рождения", null=True, default='null')  # Год рождения
    email = models.EmailField(verbose_name="email_0", null=True)  # электронная почта 0
    email_1 = models.EmailField(verbose_name="email_1", null=True, default='null')  # электронная почта 1
    email_2 = models.EmailField(verbose_name="email_2", null=True, default='null')  # электронная почта 2
    phone = models.CharField(verbose_name="phone", null=True)  # телефон 1
    phone_3 = models.CharField(max_length=255, verbose_name="phone_3", null=True, default='null')  # телефон 3
    phone_4 = models.CharField(max_length=255, verbose_name="phone_4", null=True, default='null')  # телефон 4
    country = models.CharField(max_length=255, verbose_name="Страна", null=True)  # Страна RU
    ct = models.CharField(max_length=255, verbose_name="Город", null=True, default='null')  # Город
    st = models.CharField(max_length=255, verbose_name="Область", null=True, default='null')  # Штат
    zipzip = models.CharField(max_length=255, verbose_name="Индекс", null=True, default='null')  # Индекс
    madid = models.CharField(max_length=255, verbose_name="madid", null=True, default='null')  # Какой-то айдишник
    uid = models.IntegerField(verbose_name="Facebook ID", null=True,
                              default=0)  # Каждому пользователю Facebook, приписывается уникальный ID пользователя (UID)
    value = models.IntegerField(verbose_name="Сумма покупки", null=True, default=0)  # Сумма покупки?
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name="published", null=True)
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return str(self.name)


class Private_person(models.Model):
    class Meta:
        verbose_name = "Заказчик физлицо"
        verbose_name_plural = "Физ.лица "

    customername = models.CharField(max_length=255, verbose_name="ФИО", null=True, default='null')
    mail = models.EmailField(verbose_name="email", null=True, default='null')
    passportnumber = models.CharField(max_length=255, verbose_name="Паспорт", null=True, default='null')
    issued = models.CharField(max_length=255, verbose_name="Кем выдан", null=True, default='null')
    whenissued = models.DateField(verbose_name="Когда выдан", null=True, default='null')
    placeofregistration = models.CharField(max_length=255, verbose_name="Место регистрации", null=True, default='null')
    telephonenum = models.CharField(max_length=255, verbose_name="Телефон", null=True, default='null')
    def __str__(self):
        return str(self.customername)
