from django.db import models

# Create your models here.
class Lids(models.Model):
    class Meta:
        verbose_name = "Лиды"
        verbose_name_plural = "Входящие заявки"
    name = models.CharField(max_length=100,verbose_name="name", null=True,default="unknown")
    email = models.EmailField(verbose_name="email", null=True,default="unknown")
    town = models.CharField(max_length=100,verbose_name="town", null=True,default="unknown")
    telephone = models.CharField(max_length=20,verbose_name="phone", null=True,default="unknown")
    area = models.IntegerField(verbose_name="area", null=True, default=0)
    description = models.TextField(verbose_name="description", null=True,default="unknown")
    source = models.TextField(verbose_name="source", null=True)
    what_service = models.CharField(max_length=100,verbose_name="service", null=True,default="unknown")
    our_price = models.IntegerField(verbose_name="price", null=True, default=0)
    new = models.IntegerField(verbose_name="is new?", null=True, default=0)
    date_now = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name="date", null=True)
    result = models.TextField(verbose_name="result", null=True, default="no result")
    id = models.AutoField(primary_key = True)