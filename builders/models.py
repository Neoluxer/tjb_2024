from django.db import models


# Create your models here.
class Builders(models.Model):
    class Meta:
        verbose_name = "Builders organisation"
        verbose_name_plural = "builders"

    ct = models.CharField(max_length=255, verbose_name="town", null=True, default='null')  # Город
    fn = models.CharField(max_length=255, verbose_name="familia", null=True, default='null')  # Фамилия
    name = models.CharField(verbose_name="name", max_length=255)  # Имя
    ln = models.CharField(max_length=255, verbose_name="last_name", null=True, default='null')  # Отчество
    specialisation = models.CharField(max_length=255, verbose_name="specialisation", null=True, default='null')  # Специализация
    phone = models.CharField(verbose_name="phone", null=True)  # телефон 1
    email = models.EmailField(verbose_name="email_0", null=True)  # электронная почта 0
    site = models.URLField(verbose_name="site", null=True) # Сайт
    social_media = models.CharField(verbose_name="social medias", null=True)  # социальные сети
    organisation_name = models.CharField(max_length=255, verbose_name="organisation name", null=True,                                        default='null')  # Название
    country = models.CharField(max_length=255, verbose_name="country", null=True)  # Страна RU
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name="published", null=True)
    id = models.AutoField(primary_key=True)
    price = models.IntegerField(verbose_name='price per meter', null=True, default=1)
    portfolio_image = models.ImageField(upload_to='files/', default='DEFAULT VALUE',
                                    verbose_name='example of work',
                                    null=True)
    segment = models.CharField(verbose_name="price segment", max_length=255, null=True, default='econom')
    legal_form = models.CharField(verbose_name="legal form", max_length=255, null=True, default='IP')
    note = models.TextField(verbose_name="note", null=True) # Примечание
    make_an_estimate = models.BooleanField(verbose_name="make an estimate",default=False)
    make_an_management = models.BooleanField(verbose_name="project management", default=False)
    work_on_the_project = models.BooleanField(verbose_name="work on the project", default=False)
    commission = models.BooleanField(verbose_name="give commissions", default=False)
    organisation_structure = models.BooleanField(verbose_name="there is an organizational structure", default=False)
    have_complectation = models.BooleanField(verbose_name="there is a supplier", default=False)
    order = models.BooleanField(verbose_name="there is order at the working area", default=False)
    universal = models.BooleanField(verbose_name="work with universal", default=False)
    stock = models.BooleanField(verbose_name="there is a warehouse", default=False)
    quality = models.BooleanField(verbose_name="internal quality control", default=False)
    in_work = models.IntegerField(verbose_name='objects in operation', null=True, default=1)
    working_time = models.IntegerField(verbose_name='experience', null=True, default=1)


    def __str__(self):
        return str(self.name)
