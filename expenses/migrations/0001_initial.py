# Generated by Django 4.2.4 on 2024-03-08 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AddExpenses',
            fields=[
                ('description', models.TextField(null=True, verbose_name='description')),
                ('price', models.FloatField(null=True, verbose_name='price')),
                ('published', models.DateField(auto_now_add=True, db_index=True, null=True, verbose_name='published')),
                ('category', models.IntegerField(default=0, null=True, verbose_name='category')),
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name': 'Расход денежных средств',
                'verbose_name_plural': 'Расходы ',
            },
        ),
    ]