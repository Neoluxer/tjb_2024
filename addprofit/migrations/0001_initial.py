# Generated by Django 4.2.4 on 2024-02-07 14:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer_category',
            fields=[
                ('name', models.CharField(db_index=True, max_length=250, unique=True, verbose_name='Заказчик')),
                ('id', models.AutoField(db_index=True, primary_key=True, serialize=False, verbose_name='id')),
            ],
            options={
                'verbose_name': 'Заказчик',
                'verbose_name_plural': 'Заказчики',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='AddProfits',
            fields=[
                ('description', models.TextField(null=True, verbose_name='description')),
                ('price', models.FloatField(null=True, verbose_name='price')),
                ('published', models.DateField(auto_now_add=True, db_index=True, null=True, verbose_name='published')),
                ('category', models.IntegerField(default=0, null=True, verbose_name='category')),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='addprofit.customer_category', verbose_name='Заказчик')),
            ],
            options={
                'verbose_name': 'Поступления денежных средств',
                'verbose_name_plural': 'Доходы ',
            },
        ),
    ]
