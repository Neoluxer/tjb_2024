from datetime import date

import finplan_constants
from Classes.CalcClasses import ProjectPrice
from contract_generator import *


def full_design_project():
    """
    Состав услуги Полный дизайн-проект списком
    """
    return ['обмеры',
            'электрика',
            'планировка',
            'кладочный план',
            'демонтаж',
            'план ТП',
            'развертки',
            'ведомость',
            'план пола',
            'план потолка',
            'мебельные конструкции',
            'визуализация',
            'обложка',
            'электрика освещение',
            'электрика розетки',
            'узлы потолка',
            'примечание',
            'ведомость электроустановки',
            'ведомость дверей',
            'схема разверток стен',
            'cхема сан.тех.приборов',
            ]


def full_design_project_complectation():
    """
    Состав услуги Полный дизайн-проект с комплектацией списком
    """
    complectation = ['комплектация']
    new_list = list(full_design_project()) + complectation
    return new_list


def foreproject():
    """
    Состав услуги фор-проект списком
    """
    return ['фор-проект']


def full_design_project_supervision():
    """
    Состав услуги Полный дизайн-проект с авторским надзором
    """
    supervision = ['авторский надзор']
    new_list = list(full_design_project()) + supervision
    return new_list


def content_modificator(data_set, index):
    """
    В зависимости от данных из столбца compound возвращает список с набором услуг в том, виде,
    который поддерживает класс ProjectPrice
    """
    content_value = (data_set.iloc[index]["compound"])
    swich = {"полный дизайн проект": full_design_project(),
             "проект с комплектацией": full_design_project_complectation(),
             "форпроект": foreproject(),
             "проект с авторским надзором": full_design_project_supervision()}
    return swich.get(content_value, [content_value])


def designers_calculator(area: int) -> float:
    """
    Считает сколько нужно дизайнеров на дизайн-проект
    """
    return area / finplan_constants.NORM_AREA_FOR_DESIGNER


def draftsmens_calculator(area: int) -> float:
    """
    Считает количество проектировщиков исходя из площади
    """
    # if area <= 200:
    #     return 1
    # elif 400 >= area > 200:
    #     return 2
    # elif area >= 2000:
    #     return round(area / 300, 0)
    # else:
    #     return round(area / 200, 0)
    return area / finplan_constants.NORM_AREA_FOR_DRAFTSMEN


def calendar(first_date, second_date):
    date_list = []
    delta = second_date - first_date
    for i in range(delta.days + 1):
        data_formated_string = f"{str((first_date + timedelta(i)).year)}-{str((first_date + timedelta(i)).month)}"
        date_list.append(data_formated_string)
    return sorted(list(set(date_list)))


def calendar_empty_dict(first_date, second_date):
    """
    Создает пустой календарь платежей за период для дальнейшего заполнения данными
    """
    list_of_dates = calendar(first_date, second_date)
    a = int(len(list_of_dates))
    list_of_null_values = [0] * a
    return dict(zip(list_of_dates, list_of_null_values))


def calendar_dict_from_instance_list(dataset):
    """
    Создает словарь с платежами из генератора заказов
    from_data_set_to_list_pp_instance
    """
    payments_dict = calendar_empty_dict(date(2024, 1, 1), date(2027, 1, 1))
    all_instance = from_data_set_to_list_pp_instance(dataset)

    for items in all_instance:
        for values in items.full_project_payments_calendar().keys():
            if values in payments_dict:
                if (payments_dict[values]) == 0:  # Если нет никакой записи
                    payments_dict[values] = items.full_project_payments_calendar()[values]
                else:
                    old_value = payments_dict[values]
                    new_value = old_value + items.full_project_payments_calendar()[values]
                    payments_dict[values] = new_value

            else:
                pass
                print(f'{values} is not in dict with value: {items.full_project_payments_calendar().get(values)}')

    return payments_dict


def from_data_set_to_list_pp_instance(dt_set):
    """
    Создает список с экземплярами класса ProjectPrice из dataset contract_dataset_generator
    """

    contracts = [ProjectPrice(square=int(dt_set.at[i, "area"]),
                              spaces=int(dt_set.iloc[i]["area"]) / finplan_constants.MIDDLE_ROOM,
                              typeof=1,
                              date_start=dt_set.at[i, "data"],
                              content=content_modificator(dt_set, i),
                              designers=designers_calculator(int(dt_set.at[i, "area"])),
                              draftsmen=draftsmens_calculator(int(dt_set.at[i, "area"]))) for i in
                 range(len(dt_set))]

    return contracts


if __name__ == '__main__':
    d1 = '1.1.2025'  # начальная дата
    d2 = '1.1.2026'  # конечная дата
    contracts_dataset = contract_dataset_generator(15, d1, d2)
    print()
    print(calendar_dict_from_instance_list(contracts_dataset))
