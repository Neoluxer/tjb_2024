import random
from datetime import datetime as dt
from datetime import timedelta

import pandas as pd

default_contract = pd.DataFrame(columns=['area', 'compound', 'price', 'data'])


def random_options(list_options):
    return random.choice(list_options)


def options_generator(numbers, list_of_options):
    new_options_list = []
    for n in range(0, numbers):
        new_options_list.append(random_options(list_of_options))
    return new_options_list


def area_generator(numbers, area_min, area_max):
    new_area_list = []
    for n in range(0, numbers):
        new_area_list.append(int(random.uniform(area_min, area_max)))
    return new_area_list


def get_random_date(start, end):
    delta = end - start
    random_data = start + timedelta(random.randint(0, delta.days))
    return random_data


def data_list_generator(numbers, start, end):
    start_dt = dt.strptime(start, '%d.%m.%Y')
    end_dt = dt.strptime(end, '%d.%m.%Y')
    data_list = []
    for _ in range(numbers):
        data_list.append(get_random_date(start_dt, end_dt))
    return data_list


def contract_dataset_generator(numbers, start, end, list_of_options, area_min, area_max):
    """
    @return Генерируются рандомные проекты в виде dataset
    """
    for items in range(numbers):
        default_contract.loc[len(default_contract.index)] = [int(area_generator(numbers, area_min, area_max)[items]),
                                                             options_generator(numbers, list_of_options)[items],
                                                             3500,
                                                             data_list_generator(numbers, start, end)[items].date()]
    return default_contract


if __name__ == '__main__':
    new_kit_2032 = (contract_dataset_generator(77, '01.01.2030', '29.12.2030', ['фор-проект', 'проект с комплектацией',
                                                                                'полный дизайн проект', 'планировка',
                                                                                'проект с авторским надзором'], 40,
                                               200))
    with pd.ExcelWriter('XLSX/testdoc_2027.xlsx', mode="a", engine="openpyxl") as writer:
        new_kit_2032.to_excel(writer, sheet_name="2032", index=False)
