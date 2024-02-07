# Не оптимизировать импорты и не менять их порядок

import os

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dj_ac.settings")
os.environ.update({'DJANGO_ALLOW_ASYNC_UNSAFE': "true"})
django.setup()

import logging
from asgiref.sync import sync_to_async
from addprofit.models import AddProfits, Customer_category
from django.db.models import Min, Max

logger = logging.getLogger(__name__)


# Минимальная прибыль:
@sync_to_async
def get_profit_min_price():
    from django.db.models import Min
    min_price = AddProfits.objects.aggregate(Min('price'))
    return min_price.popitem()[1]


# Максимальная прибыль:
@sync_to_async
def get_profit_max_price():
    from django.db.models import Max
    max_price = AddProfits.objects.aggregate(Max('price'))
    return max_price.popitem()[1]


# Сумма прибылей:
@sync_to_async
def get_sum_all_prices():
    all_profits_count = AddProfits.objects.filter(price__gte=1)
    list_op = []
    for b in all_profits_count:
        list_op.append(b.price)
    return sum(list_op)


@sync_to_async
def get_id_from_customer_name(customer_id):
    customers = Customer_category.objects.filter(name__exact=customer_id)
    return customers.values().first()['id']


# Фильтр по году:
@sync_to_async
def get_sum_is_year(year):
    all_profits_count = AddProfits.objects.filter(published__year=year)
    list_op = []
    for b in all_profits_count:
        list_op.append(b.price)
    return sum(list_op)


@sync_to_async
def average_profit():
    def all_profits():
        all_profits_count = AddProfits.objects.filter(price__gte=1)
        list_op = []
        for b in all_profits_count:
            list_op.append(b.price)
        return sum(list_op)

    def counting_months():
        min_date = AddProfits.objects.aggregate(Min('published'))
        max_date = AddProfits.objects.aggregate(Max('published'))
        days = (max_date.popitem()[1]) - (min_date.popitem()[1])
        return int(days.days / 30)

    gs = all_profits()
    numbers = counting_months()
    return int(gs / numbers)


# 30,417
@sync_to_async
def counting_all_months():
    min_date = AddProfits.objects.aggregate(Min('published'))
    max_date = AddProfits.objects.aggregate(Max('published'))
    days = (max_date.popitem()[1]) - (min_date.popitem()[1])
    return int(days.days / 30)


# Фильтр по источнику:
@sync_to_async
def get_sum_is_source(source):
    all_profits_count = AddProfits.objects.filter(category__exact=source)
    list_op = []
    for b in all_profits_count:
        list_op.append(b.price)
    return sum(list_op)


# Фильтр по заказчику id:
@sync_to_async
def get_sum_is_customer(customer):
    all_profits_count = AddProfits.objects.filter(customer_id__exact=customer)
    list_op = []
    for b in all_profits_count:
        list_op.append(b.price)
    return sum(list_op)


@sync_to_async
def get_sum_is_customer_name(cname):
    def customer_name(cname):
        customers = Customer_category.objects.filter(name__exact=cname)
        return customers.values().first()['id']

    cust_id = customer_name(cname)

    def get_sum_is_customer(cust_id):
        all_profits_count = AddProfits.objects.filter(customer_id__exact=cust_id)
        list_op = []
        for b in all_profits_count:
            list_op.append(b.price)
        return sum(list_op)

    return get_sum_is_customer(cust_id)


# Фильтр по году и месяцу:
@sync_to_async
def get_sum_is_month(year, month):
    all_profits_count = AddProfits.objects.filter(published__year=year, published__month=month)
    list_op = []
    for b in all_profits_count:
        list_op.append(b.price)
    return sum(list_op)


# Разница с доходом прошлого года:
@sync_to_async
def get_difference_is_month(year, month):
    all_profits_count_1 = AddProfits.objects.filter(published__year=year + 1, published__month=month)
    list_op = []
    for b in all_profits_count_1:
        list_op.append(b.price)
    first = sum(list_op)
    print(first)

    all_profits_count_2 = AddProfits.objects.filter(published__year=year, published__month=month)
    list_op_2 = []
    for b in all_profits_count_2:
        list_op_2.append(b.price)
    second = sum(list_op_2)
    return first - second


# Считает сколько составляет та или иная категория дохода в заданный период в процентах
@sync_to_async
def percentage_of_income_for_period(year, month, category):
    def profit_from_all_categories():
        all_profits_count_all_category = AddProfits.objects.filter(published__year=year, published__month=month)
        list_op_3 = []
        for b in all_profits_count_all_category:
            list_op_3.append(b.price)
        result_category = sum(list_op_3)
        print(f'result_category {result_category}')
        return result_category

    def profit_from_one_category():
        all_profits_count_category = AddProfits.objects.filter(published__year=year, published__month=month,
                                                               category__exact=category)
        list_op_4 = []
        for b in all_profits_count_category:
            list_op_4.append(b.price)
        print(f'result_category {sum(list_op_4)}')
        return sum(list_op_4)
    try:
        one_proc = profit_from_all_categories() / 100
        result = profit_from_one_category() / one_proc


    except:
        result = profit_from_one_category() / 1
    return result

if __name__ == '__main__':
    pass
    # print(percentage_of_income_for_period(year=2023,month=11,category=3))
