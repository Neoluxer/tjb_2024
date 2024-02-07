# Generated by Django 4.2.4 on 2024-02-07 14:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('addprofit', '0001_initial'),
        ('make_contract_base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('invoice_file', models.FileField(default='DEFAULT VALUE', null=True, upload_to='files/', verbose_name='Путь к файлу (акт)')),
                ('invoice_file_invoice', models.FileField(default='DEFAULT VALUE', null=True, upload_to='files/', verbose_name='Путь к файлу (счёт)')),
                ('name', models.CharField(max_length=255, null=True, verbose_name='Основание платежа')),
                ('published', models.DateField(db_index=True, null=True, verbose_name='Дата')),
                ('sum', models.IntegerField(null=True, verbose_name='Сумма')),
                ('invoice_number', models.CharField(default='null', max_length=50, null=True, verbose_name='Номер счета')),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='addprofit.customer_category', verbose_name='Заказчик')),
                ('organisation', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='make_contract_base.organization', verbose_name='Организация')),
                ('ruberic', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='make_contract_base.contractbase', verbose_name='Номер договора')),
            ],
            options={
                'verbose_name': 'Счёт',
                'verbose_name_plural': 'Счета ',
            },
        ),
    ]
