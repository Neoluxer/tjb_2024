import collections
import datetime

from Advertising import AdvertisingGeneratesLeads
from conveyor_of_contract_instance import *

date_columns = ['Месяц 1', 'Месяц 2', 'Месяц 3', 'Месяц 4', 'Месяц 5', 'Месяц 6', 'Месяц 7', 'Месяц 8',
                'Месяц 9', 'Месяц 10', 'Месяц 11', 'Месяц 12']
default_contract = pd.DataFrame(
    columns=['Показатель', 'Месяц 1', 'Месяц 2', 'Месяц 3', 'Месяц 4', 'Месяц 5', 'Месяц 6', 'Месяц 7', 'Месяц 8',
             'Месяц 9', 'Месяц 10', 'Месяц 11', 'Месяц 12', 'Итого', 'Константы'])


def insert_profit_to_first_index(month, profit, contract):
    """Добавляет доход от проектов в таблицу по месяцам в первую строку"""
    month = f'Месяц {month}'
    contract.at[0, month] = profit


def calc_month_workers_expense(contract_list):
    expense_dict = []
    if (len(contract_list)) > 0:
        for m in range(0, 12):
            if len(contract_list[m]) > 0:
                for n in range(0, len(contract_list[m])):
                    compound = contract_list[m]['compound'].values[n]

                    if contract_list[m]['compound'].values[n] == 'фор-проект':
                        area = contract_list[m]['area'].values[n]
                        sum_of_expenses = int(area) * int(ProjectPrice.WAGE_OF_DRAFTSMEN_FP)
                        expense_dict.append([sum_of_expenses, m + 1])

                    elif compound == 'проект с комплектацией':
                        area = contract_list[m]['area'].values[n]
                        sum_of_expenses = int(area) * (
                                int(ProjectPrice.WAGE_OF_DESIGNER) + int(ProjectPrice.WAGE_OF_DRAFTSMEN))
                        expense_dict.append([sum_of_expenses, m + 1])

                    elif compound == 'планировка':
                        area = contract_list[m]['area'].values[n]
                        sum_of_expenses = int(area) * (int(ProjectPrice.WAGE_OF_DRAFTSMEN_P))
                        expense_dict.append([sum_of_expenses, m + 1])

                    elif compound == 'полный дизайн проект':
                        area = contract_list[m]['area'].values[n]
                        sum_of_expenses = int(area) * (int(ProjectPrice.WAGE_OF_DRAFTSMEN) +
                                                       int(ProjectPrice.WAGE_OF_DESIGNER))
                        expense_dict.append([sum_of_expenses, m + 1])

                    elif compound == 'проект с авторским надзором':
                        area = contract_list[m]['area'].values[n]
                        sum_of_expenses = int(area) * (int(ProjectPrice.WAGE_OF_DRAFTSMEN) +
                                                       int(ProjectPrice.WAGE_OF_DESIGNER))
                        expense_dict.append([sum_of_expenses, m + 1])
                    else:
                        pass
            else:
                pass
    return expense_dict


def make_contract_list(contract_dataset, year):
    """
    @param contract_dataset: dtype
    @type contract_dataset: dtype
    @param year: int
    @type year: int
    @return: list 12 dtype с данными отсортированными по месяцам
    @rtype: list
    """
    contract_list = []
    january = (contract_dataset.loc[(contract_dataset['data'] >= datetime.date(year=year, month=1, day=1)) &
                                    (contract_dataset['data'] <= datetime.date(year=year, month=1, day=30))])
    february = (contract_dataset.loc[(contract_dataset['data'] >= datetime.date(year=year, month=2, day=1)) &
                                     (contract_dataset['data'] <= datetime.date(year=year, month=2, day=28))])
    march = (contract_dataset.loc[(contract_dataset['data'] >= datetime.date(year=year, month=3, day=1)) &
                                  (contract_dataset['data'] <= datetime.date(year=year, month=3, day=31))])
    april = (contract_dataset.loc[(contract_dataset['data'] >= datetime.date(year=year, month=4, day=1)) &
                                  (contract_dataset['data'] <= datetime.date(year=year, month=4, day=30))])
    may = (contract_dataset.loc[(contract_dataset['data'] >= datetime.date(year=year, month=5, day=1)) &
                                (contract_dataset['data'] <= datetime.date(year=year, month=5, day=30))])
    june = (contract_dataset.loc[(contract_dataset['data'] >= datetime.date(year=year, month=6, day=1)) &
                                 (contract_dataset['data'] <= datetime.date(year=year, month=6, day=30))])
    july = (contract_dataset.loc[(contract_dataset['data'] > datetime.date(year=year, month=7, day=1)) &
                                 (contract_dataset['data'] <= datetime.date(year=year, month=7, day=30))])
    august = (contract_dataset.loc[(contract_dataset['data'] >= datetime.date(year=year, month=8, day=1)) &
                                   (contract_dataset['data'] <= datetime.date(year=year, month=8, day=30))])
    september = (contract_dataset.loc[(contract_dataset['data'] >= datetime.date(year=year, month=9, day=1)) &
                                      (contract_dataset['data'] <= datetime.date(year=year, month=9, day=30))])
    october = (contract_dataset.loc[(contract_dataset['data'] >= datetime.date(year=year, month=10, day=1)) &
                                    (contract_dataset['data'] <= datetime.date(year=year, month=10, day=30))])
    november = (contract_dataset.loc[(contract_dataset['data'] >= datetime.date(year=year, month=11, day=1)) &
                                     (contract_dataset['data'] <= datetime.date(year=year, month=11, day=30))])
    december = (contract_dataset.loc[(contract_dataset['data'] >= datetime.date(year=year, month=12, day=1)) &
                                     (contract_dataset['data'] <= datetime.date(year=year, month=12, day=30))])
    contract_list.append(january)
    contract_list.append(february)
    contract_list.append(march)
    contract_list.append(april)
    contract_list.append(may)
    contract_list.append(june)
    contract_list.append(july)
    contract_list.append(august)
    contract_list.append(september)
    contract_list.append(october)
    contract_list.append(november)
    contract_list.append(december)
    return contract_list


def add_sum_to_finplan(contract, profit_list):
    for items in date_columns:
        if items.title() == 'Месяц 1':
            contract.at[8, 'Месяц 1'] = profit_list[0]
        elif items.title() == 'Месяц 2':
            contract.at[8, 'Месяц 2'] = profit_list[1]
        elif items.title() == 'Месяц 3':
            contract.at[8, 'Месяц 3'] = profit_list[2]
        elif items.title() == 'Месяц 4':
            contract.at[8, 'Месяц 4'] = profit_list[3]
        elif items.title() == 'Месяц 5':
            contract.at[8, 'Месяц 5'] = profit_list[4]
        elif items.title() == 'Месяц 6':
            contract.at[8, 'Месяц 6'] = profit_list[5]
        elif items.title() == 'Месяц 7':
            contract.at[8, 'Месяц 7'] = profit_list[6]
        elif items.title() == 'Месяц 8':
            contract.at[8, 'Месяц 8'] = profit_list[7]
        elif items.title() == 'Месяц 9':
            contract.at[8, 'Месяц 9'] = profit_list[8]
        elif items.title() == 'Месяц 10':
            contract.at[8, 'Месяц 10'] = profit_list[9]
        elif items.title() == 'Месяц 11':
            contract.at[8, 'Месяц 11'] = profit_list[10]
        elif items.title() == 'Месяц 12':
            contract.at[8, 'Месяц 12'] = profit_list[11]


def add_piggy_bank_to_fin_plan(contract):
    for items in date_columns:
        contract.at[9, items] = (int(contract[items].iloc[0]) * float(ProjectPrice.TO_THE_PIGGY_BANK))  # Копилка 30%


def add_coast_full_project_to_fp(contract):
    abstract_project = ProjectPrice(square=100, spaces=8, typeof=1, content=['обмеры',
                                                                             'электрика',
                                                                             'планировка',
                                                                             'кладочный план',
                                                                             'демонтаж',
                                                                             'план ТП',
                                                                             'ведомость',
                                                                             'план пола',
                                                                             'план потолка',
                                                                             'мебельные конструкции',
                                                                             'обложка',
                                                                             'электрика освещение',
                                                                             'электрика розетки',
                                                                             'узлы потолка',
                                                                             'примечание',
                                                                             'ведомость электроустановки',
                                                                             'ведомость дверей',
                                                                             'схема разверток стен',
                                                                             'cхема сан.тех.приборов',
                                                                             'развертки',
                                                                             'визуализация', ],
                                    designers=2,
                                    draftsmen=2)
    price = abstract_project.overhead()
    for items in date_columns:
        contract.at[10, items] = price


def add_counter_new_projects(contract, list_1, list_2, list_3, list_4, list_5, list_6, list_7, list_8, list_9, list_10,
                             list_11, list_12):
    for items in date_columns:
        if items.title() == 'Месяц 1':
            contract.at[11, 'Месяц 1'] = len(list_1)
        elif items.title() == 'Месяц 2':
            contract.at[11, 'Месяц 2'] = len(list_2)
        elif items.title() == 'Месяц 3':
            contract.at[11, 'Месяц 3'] = len(list_3)
        elif items.title() == 'Месяц 4':
            contract.at[11, 'Месяц 4'] = len(list_4)
        elif items.title() == 'Месяц 5':
            contract.at[11, 'Месяц 5'] = len(list_5)
        elif items.title() == 'Месяц 6':
            contract.at[11, 'Месяц 6'] = len(list_6)
        elif items.title() == 'Месяц 7':
            contract.at[11, 'Месяц 7'] = len(list_7)
        elif items.title() == 'Месяц 8':
            contract.at[11, 'Месяц 8'] = len(list_8)
        elif items.title() == 'Месяц 9':
            contract.at[11, 'Месяц 9'] = len(list_9)
        elif items.title() == 'Месяц 10':
            contract.at[11, 'Месяц 10'] = len(list_10)
        elif items.title() == 'Месяц 11':
            contract.at[11, 'Месяц 11'] = len(list_11)
        elif items.title() == 'Месяц 12':
            contract.at[11, 'Месяц 12'] = len(list_12)


def add_counter_of_fp(contract, contract_dataset):
    contract.at[12, 'Итого'] = sum_row_case_condition(contract_dataset, 'фор-проект')


def add_counter_of_dp(contract, contract_dataset):
    contract.at[13, 'Итого'] = sum_row_case_condition(contract_dataset, 'полный дизайн проект')


def add_counter_of_dp_complectation(contract, contract_dataset):
    contract.at[14, 'Итого'] = sum_row_case_condition(contract_dataset, 'проект с комплектацией')


def add_counter_of_dp_inspection(contract, contract_dataset):
    contract.at[15, 'Итого'] = sum_row_case_condition(contract_dataset, 'проект с авторским надзором')


def add_counter_of_plans(contract, contract_dataset):
    contract.at[16, 'Итого'] = sum_row_case_condition(contract_dataset, 'планировка')


def add_summ_of_projects(contract):
    contract.at[11, 'Итого'] = "=СУММ(C13:N13)"


def add_potential_building_profit(contract, contract_dataset):
    value = contract['Итого'].iloc[13]
    value2 = contract['Итого'].iloc[14]
    value3 = contract['Итого'].iloc[15]
    all_areas = value + value2 + value3
    result = (all_areas * finplan_constants.POTENTIAL_PROFIT_BUILDING_PER_METER)
    contract.at[17, 'Итого'] = result


def add_summ_of_all_reserv(contract):
    contract.at[9, 'Итого'] = "=СУММ(C11:N11)\n\n "


def add_summ_of_all_profit(contract):
    contract.at[8, 'Итого'] = "=СУММ(C10:N10)\n\n "


def add_summ_of_all_ad(contract):
    contract.at[7, 'Итого'] = "=СУММ(C9:N9)\n\n "


def add_summ_of_all_fot(contract):
    contract.at[6, 'Итого'] = "=СУММ(C8:N8)\n\n "


def add_summ_of_all_bank_comission(contract):
    contract.at[5, 'Итого'] = "=СУММ(C7:N7)\n\n "


def add_summ_of_all_director_wage(contract):
    contract.at[4, 'Итого'] = "=СУММ(C6:N6)\n\n "


def add_summ_of_all_hosting(contract):
    contract.at[3, 'Итого'] = "=СУММ(C5:N5)\n\n "


def add_summ_of_all_tax(contract):
    contract.at[2, 'Итого'] = "=СУММ(C4:N4)\n\n "


def add_summ_of_all_buh(contract):
    contract.at[1, 'Итого'] = "=СУММ(C3:N3)\n\n "


def add_summ_of_all_income(contract):
    contract.at[0, 'Итого'] = "=СУММ(C2:N2)\n\n "


def add_constants(contract, counter_n_p):
    sum_proj = 0
    for items in counter_n_p:
        sum_proj += len(items)

    contract.at[18, 'Показатель'] = 'Конверсия в покупателя'
    contract.at[18, 'Константы'] = finplan_constants.CONVERSION_TO_CUSTOMER
    contract.at[19, 'Показатель'] = 'Чертёжнику за м.кв. полного проекта'
    contract.at[19, 'Константы'] = finplan_constants.WAGE_OF_DRAFTSMEN
    contract.at[20, 'Показатель'] = 'Дизайнеру (визуализатору) за м.кв. полного проекта'
    contract.at[20, 'Константы'] = finplan_constants.WAGE_OF_DESIGNER
    contract.at[21, 'Показатель'] = 'Чертёжнику за м.кв Фор-Проекта'
    contract.at[21, 'Константы'] = ProjectPrice.WAGE_OF_DRAFTSMEN_FP
    contract.at[22, 'Показатель'] = 'Чертёжнику за м.кв Планировки'
    contract.at[22, 'Константы'] = ProjectPrice.WAGE_OF_DRAFTSMEN_P
    contract.at[23, 'Показатель'] = 'Норма прибыли в месяц (рубли)'
    contract.at[23, 'Константы'] = ProjectPrice.PROFIT_NORM_PER_M
    contract.at[24, 'Показатель'] = 'Привлечено подписчиков'
    contract.at[24, 'Итого'] = sum_proj / finplan_constants.CONVERSION_TO_CUSTOMER
    contract.at[25, 'Показатель'] = 'Норма площади на одного дизайнера в месяц'
    contract.at[25, 'Константы'] = finplan_constants.NORM_AREA_FOR_DESIGNER
    contract.at[26, 'Показатель'] = 'Кол-во дизайнеров'
    contract.at[27, 'Показатель'] = 'Кол-во чертёжников'
    contract.at[28, 'Показатель'] = 'Расход на арт-директора'


def add_designers_and_draftsmens(contract, param):
    #print(f" add_designers_and_draftsmens {param}")
    for items in date_columns:
        if items.title() == 'Месяц 1':
            contract.at[26, 'Месяц 1'] = param[0][2]
            contract.at[27, 'Месяц 1'] = param[0][1]
            if param[0][2]>10:
                artdirectors_1 = round(int(param[0][2])/5,0)
                contract.at[28, 'Месяц 1'] = (artdirectors_1*40_000)*-1
            else:
                contract.at[28, 'Месяц 1'] =0
        elif items.title() == 'Месяц 2':
            contract.at[26, 'Месяц 2'] = param[1][2]
            contract.at[27, 'Месяц 2'] = param[1][1]
            if param[1][2]>10:
                artdirectors_1 = round(int(param[1][2])/5,0)
                contract.at[28, 'Месяц 2'] = (artdirectors_1*40_000)*-1
            else:
                contract.at[28, 'Месяц 2'] =0
        elif items.title() == 'Месяц 3':
            contract.at[26, 'Месяц 3'] = param[2][2]
            contract.at[27, 'Месяц 3'] = param[2][1]
            if param[2][2]>10:
                artdirectors_1 = round(int(param[2][2])/5,0)
                contract.at[28, 'Месяц 3'] = (artdirectors_1*40_000)*-1
            else:
                contract.at[28, 'Месяц 3'] =0
        elif items.title() == 'Месяц 4':
            contract.at[26, 'Месяц 4'] = param[3][2]
            contract.at[27, 'Месяц 4'] = param[3][1]
            if param[3][2]>10:
                artdirectors_1 = round(int(param[3][2])/5,0)
                contract.at[28, 'Месяц 4'] = (artdirectors_1*40_000)*-1
            else:
                contract.at[28, 'Месяц 4'] =0
        elif items.title() == 'Месяц 5':
            contract.at[26, 'Месяц 5'] = param[4][2]
            contract.at[27, 'Месяц 5'] = param[4][1]
            if param[4][2]>10:
                artdirectors_1 = round(int(param[4][2])/5,0)
                contract.at[28, 'Месяц 5'] = (artdirectors_1*40_000)*-1
            else:
                contract.at[28, 'Месяц 5'] =0
        elif items.title() == 'Месяц 6':
            contract.at[26, 'Месяц 6'] = param[5][2]
            contract.at[27, 'Месяц 6'] = param[5][1]
            if param[5][2]>10:
                artdirectors_1 = round(int(param[5][2])/5,0)
                contract.at[28, 'Месяц 6'] = (artdirectors_1*40_000)*-1
            else:
                contract.at[28, 'Месяц 6'] =0
        elif items.title() == 'Месяц 7':
            contract.at[26, 'Месяц 7'] = param[6][2]
            contract.at[27, 'Месяц 7'] = param[6][1]
            if param[6][2]>10:
                artdirectors_1 = round(int(param[6][2])/5,0)
                contract.at[28, 'Месяц 7'] = (artdirectors_1*40_000)*-1
            else:
                contract.at[28, 'Месяц 7'] =0
        elif items.title() == 'Месяц 8':
            contract.at[26, 'Месяц 8'] = param[7][2]
            contract.at[27, 'Месяц 8'] = param[7][1]
            if param[7][2]>10:
                artdirectors_1 = round(int(param[7][2])/5,0)
                contract.at[28, 'Месяц 8'] = (artdirectors_1*40_000)*-1
            else:
                contract.at[28, 'Месяц 8'] =0
        elif items.title() == 'Месяц 9':
            contract.at[26, 'Месяц 9'] = param[8][2]
            contract.at[27, 'Месяц 9'] = param[8][1]
            if param[8][2]>10:
                artdirectors_1 = round(int(param[8][2])/5,0)
                contract.at[28, 'Месяц 9'] = (artdirectors_1*40_000)*-1
            else:
                contract.at[28, 'Месяц 9'] =0
        elif items.title() == 'Месяц 10':
            contract.at[26, 'Месяц 10'] = param[9][2]
            contract.at[27, 'Месяц 10'] = param[9][1]
            if param[9][2]>10:
                artdirectors_1 = round(int(param[9][2])/5,0)
                contract.at[28, 'Месяц 10'] = (artdirectors_1*40_000)*-1
            else:
                contract.at[28, 'Месяц 10'] =0
        elif items.title() == 'Месяц 11':
            contract.at[26, 'Месяц 11'] = param[10][2]
            contract.at[27, 'Месяц 11'] = param[10][1]
            if param[10][2]>10:
                artdirectors_1 = round(int(param[10][2])/5,0)
                contract.at[28, 'Месяц 11'] = (artdirectors_1*40_000)*-1
            else:
                contract.at[28, 'Месяц 11'] =0
        elif items.title() == 'Месяц 12':
            contract.at[26, 'Месяц 12'] = param[11][2]
            contract.at[27, 'Месяц 12'] = param[11][1]
            if param[11][2]>10:
                artdirectors_1 = round(int(param[11][2])/5,0)
                contract.at[28, 'Месяц 12'] = (artdirectors_1*ProjectPrice.ART_DIRECTOR_SALARY)*-1
            else:
                contract.at[28, 'Месяц 12'] =0


def monthly_expenses(contract, contract_dataset, year):
    workers_expense = calc_month_workers_expense(make_contract_list(contract_dataset, year))
    list_1 = []
    list_2 = []
    list_3 = []
    list_4 = []
    list_5 = []
    list_6 = []
    list_7 = []
    list_8 = []
    list_9 = []
    list_10 = []
    list_11 = []
    list_12 = []
    for items in workers_expense:
        if items[1] == 1:
            list_1.append(items[0])
        elif items[1] == 2:
            list_2.append(items[0])
        elif items[1] == 3:
            list_3.append(items[0])
        elif items[1] == 4:
            list_4.append(items[0])
        elif items[1] == 5:
            list_5.append(items[0])
        elif items[1] == 6:
            list_6.append(items[0])
        elif items[1] == 7:
            list_7.append(items[0])
        elif items[1] == 8:
            list_8.append(items[0])
        elif items[1] == 9:
            list_9.append(items[0])
        elif items[1] == 10:
            list_10.append(items[0])
        elif items[1] == 11:
            list_11.append(items[0])
        elif items[1] == 12:
            list_12.append(items[0])

    """ЕЖЕМЕСЯЧНЫЕ ПОСТОЯННЫЕ РАСХОДЫ"""
    contract.at[1, 'Показатель'] = 'Оплата услуг бухгалтера'
    contract.at[2, 'Показатель'] = 'Налог на ФОТ'
    contract.at[3, 'Показатель'] = 'Хостинг сайта'
    contract.at[4, 'Показатель'] = 'Заработная плата директору'
    contract.at[5, 'Показатель'] = 'Банковская комиссия УБРИР'
    contract.at[6, 'Показатель'] = 'ФОТ исполнители'
    contract.at[7, 'Показатель'] = 'Расходы на рекламу'
    contract.at[8, 'Показатель'] = 'ИТОГО ПРИБЫЛЬ'
    contract.at[9, 'Показатель'] = 'Отложено в резерв'
    contract.at[10, 'Показатель'] = 'Стоимость за м.кв. полного д.п.'
    contract.at[11, 'Показатель'] = 'Кол-во новых проектов (шт)'
    contract.at[12, 'Показатель'] = 'Площадь фор-проектов (мкв)'
    contract.at[13, 'Показатель'] = 'Площадь дизайн-проектов (мкв)'
    contract.at[14, 'Показатель'] = 'Площадь дизайн-проектов с комплектацией (мкв)'
    contract.at[15, 'Показатель'] = 'Площадь дизайн-проектов с авторским надзором (мкв)'
    contract.at[16, 'Показатель'] = 'Площадь проектов планировок (мкв)'
    contract.at[17, 'Показатель'] = 'Потенциальный доход со стройки (10%)'

    for items in date_columns:
        contract.at[1, items] = -5000  # Оплата услуг Бухгалтерам
        contract.at[2, items] = int(ProjectPrice.OVERHEAD_PER_M) * -1  # Налог на ФОТ
        contract.at[3, items] = -2000
        contract.at[4, items] = int(ProjectPrice.DIRECTOR_SALARY) * -1  # Зарплата директору
        contract.at[5, items] = -1700 - 250 - 35 - 35 - 35 - 35  # Банковская комиссия УБРИР

        if items.title() == 'Месяц 1':
            contract.at[6, 'Месяц 1'] = sum(list_1) * -1
            contract.at[7, 'Месяц 1'] = int(finplan_constants.ADV_JAN) * -1
        elif items.title() == 'Месяц 2':
            contract.at[6, 'Месяц 2'] = sum(list_2) * -1
            contract.at[7, 'Месяц 2'] = int(finplan_constants.ADV_FE) * -1
        elif items.title() == 'Месяц 3':
            contract.at[6, 'Месяц 3'] = sum(list_3) * -1
            contract.at[7, 'Месяц 3'] = int(finplan_constants.ADV_MA) * -1
        elif items.title() == 'Месяц 4':
            contract.at[6, 'Месяц 4'] = sum(list_4) * -1
            contract.at[7, 'Месяц 4'] = int(finplan_constants.ADV_AP) * -1
        elif items.title() == 'Месяц 5':
            contract.at[6, 'Месяц 5'] = sum(list_5) * -1
            contract.at[7, 'Месяц 5'] = int(finplan_constants.ADV_MAY) * -1
        elif items.title() == 'Месяц 6':
            contract.at[6, 'Месяц 6'] = sum(list_6) * -1
            contract.at[7, 'Месяц 6'] = int(finplan_constants.ADV_JU) * -1
        elif items.title() == 'Месяц 7':
            contract.at[6, 'Месяц 7'] = sum(list_7) * -1
            contract.at[7, 'Месяц 7'] = int(finplan_constants.ADV_JUL) * -1
        elif items.title() == 'Месяц 8':
            contract.at[6, 'Месяц 8'] = sum(list_8) * -1
            contract.at[7, 'Месяц 8'] = int(finplan_constants.ADV_AU) * -1
        elif items.title() == 'Месяц 9':
            contract.at[6, 'Месяц 9'] = sum(list_9) * -1
            contract.at[7, 'Месяц 9'] = int(finplan_constants.ADV_SE) * -1
        elif items.title() == 'Месяц 10':
            contract.at[6, 'Месяц 10'] = sum(list_10) * -1
            contract.at[7, 'Месяц 10'] = int(finplan_constants.ADV_OC) * -1
        elif items.title() == 'Месяц 11':
            contract.at[6, 'Месяц 11'] = sum(list_11) * -1
            contract.at[7, 'Месяц 11'] = int(finplan_constants.ADV_NO) * -1
        elif items.title() == 'Месяц 12':
            contract.at[6, 'Месяц 12'] = sum(list_12) * -1
            contract.at[7, 'Месяц 12'] = int(finplan_constants.ADV_DE) * -1

    profit_list = sum_row(contract)
    add_sum_to_finplan(contract, profit_list)
    add_piggy_bank_to_fin_plan(contract)
    add_coast_full_project_to_fp(contract)
    counter_n_p = [list_1, list_2, list_3, list_4, list_6, list_7, list_8, list_9, list_10, list_11, list_12]
    add_counter_new_projects(contract, list_1, list_2, list_3, list_4, list_5, list_6,
                             list_7, list_8, list_9, list_10, list_11, list_12)
    add_counter_of_fp(contract, contract_dataset)
    add_counter_of_dp(contract, contract_dataset)
    add_counter_of_dp_complectation(contract, contract_dataset)
    add_counter_of_dp_inspection(contract, contract_dataset)
    add_counter_of_plans(contract, contract_dataset)
    add_summ_of_projects(contract)
    add_summ_of_all_reserv(contract)
    add_summ_of_all_profit(contract)
    add_summ_of_all_ad(contract)
    add_summ_of_all_fot(contract)
    add_summ_of_all_bank_comission(contract)
    add_summ_of_all_director_wage(contract)
    add_summ_of_all_hosting(contract)
    add_summ_of_all_tax(contract)
    add_summ_of_all_buh(contract)
    add_summ_of_all_income(contract)
    add_potential_building_profit(contract, contract_dataset)
    add_constants(contract, counter_n_p)
    result = (from_data_set_to_list_pp_instance(contract_dataset))
    add_designers_and_draftsmens(contract,add_list_of_workers_to_fp(result))

    return contract


def find_months_from_dict(dictionary, year_filter, contract):
    """Находит соответствующий месяц в таблице и передаёт в функцию
        insert_profit_to_first_index(month, profit, default_contract)
    """
    for keys, values in dictionary.items():
        year = keys.split("-")[0]
        month = keys.split("-")[1]
        profit = values
        # Добавляем в первую строчку в столбец "Показатель" :
        contract.at[0, 'Показатель'] = 'Доход от проектов'
        if str(year) == str(year_filter):
            insert_profit_to_first_index(month, profit, contract)
    return contract


def make_finplan(year):
    """Генерируем финансовый план"""

    # Генерируем дата фрейм
    # contract_dataset = cg.contract_dataset_generator(15, start_date, end_date)
    contract_dataset = customer_flow()
    print(contract_dataset)
    find_months_from_dict(calendar_dict_from_instance_list(contract_dataset), year, default_contract)
    # print(filtering_contract_dataset(datf=contract_dataset, condition_1='фор-проект'))
    contract_dataset.to_excel('XLSX/dataset_2024.xlsx', sheet_name='examination')

    return monthly_expenses(default_contract, contract_dataset, year)


def sum_row_case_condition(contract_dataset, compound):
    result = contract_dataset.loc[contract_dataset['compound'] == compound, 'area'].sum()
    return result


def sum_row(dtf):
    """

    @param dtf:
    @type dtf:
    @return: Список прибыли с Января по Декабрь
    @rtype:
    """

    dat_frame = dtf
    sum_jan = dat_frame.agg({"Месяц 1": ["sum"]})
    sum_fe = dat_frame.agg({"Месяц 2": ["sum"]})
    sum_mar = dat_frame.agg({"Месяц 3": ["sum"]})
    sum_ap = dat_frame.agg({"Месяц 4": ["sum"]})
    sum_ma = dat_frame.agg({"Месяц 5": ["sum"]})
    sum_ju = dat_frame.agg({"Месяц 6": ["sum"]})
    sum_jul = dat_frame.agg({"Месяц 7": ["sum"]})
    sum_au = dat_frame.agg({"Месяц 8": ["sum"]})
    sum_se = dat_frame.agg({"Месяц 9": ["sum"]})
    sum_ok = dat_frame.agg({"Месяц 10": ["sum"]})
    sum_no = dat_frame.agg({"Месяц 11": ["sum"]})
    sum_de = dat_frame.agg({"Месяц 12": ["sum"]})

    sum_jan_int = sum_jan.values[0][0]
    sum_fe_int = sum_fe.values[0][0]
    sum_mar_int = sum_mar.values[0][0]
    sum_ap_int = sum_ap.values[0][0]
    sum_ma_int = sum_ma.values[0][0]
    sum_ju_int = sum_ju.values[0][0]
    sum_jul_int = sum_jul.values[0][0]
    sum_au_int = sum_au.values[0][0]
    sum_se_int = sum_se.values[0][0]
    sum_ok_int = sum_ok.values[0][0]
    sum_no_int = sum_no.values[0][0]
    sum_de_int = sum_de.values[0][0]

    return [sum_jan_int, sum_fe_int, sum_mar_int, sum_ap_int, sum_ma_int, sum_ju_int, sum_jul_int, sum_au_int,
            sum_se_int, sum_ok_int, sum_no_int, sum_de_int]


def filtering_contract_dataset(datf, condition_1):
    var = datf.loc[(datf['compound'] == condition_1)]
    return var


def get_sum_of_list(result_1):
    get_sum=[]
    for items in result_1:
        if type(items)==list and sum(items)>0:
            for values in items:
                get_sum.append(values)
        elif type(items)==float:
            get_sum.append(items)
        else:
            pass
    return sum(get_sum)



def add_list_of_workers_to_fp(list_of_instance):
    dict_of_workers = []

    y = []
    f = []
    m = []
    a = []
    ma = []
    yun = []
    yu = []
    au = []
    se = []
    oc = []
    no = []
    de = []

    y_d = []
    f_d = []
    m_d = []
    a_d = []
    ma_d = []
    yun_d = []
    yu_d = []
    au_d = []
    se_d = []
    oc_d = []
    no_d = []
    de_d = []

    number = 1
    for items in list_of_instance:
        if items.date_start.month == 1 and items.date_start.year == finplan_constants.CURRENT_YEAR:
            if int(items.draftsmen)>0 and int(items.designers)>0:
                y.append(items.draftsmen)
                #print(f"items.designers  {items.designers}")
                y_d.append((items.designers))
        elif items.date_start.month == 2 and items.date_start.year == finplan_constants.CURRENT_YEAR:
            f.append(items.draftsmen)
            #print(f"items.designers  {items.designers}")
            f_d.append((items.designers))
        elif items.date_start.month == 3 and items.date_start.year == finplan_constants.CURRENT_YEAR:
            m.append(items.draftsmen)
            #print(f"items.designers  {items.designers}")
            m_d.append(items.designers)
        elif items.date_start.month == 4 and items.date_start.year == finplan_constants.CURRENT_YEAR:
            a.append(items.draftsmen)
            #print(f"items.designers  {items.designers}")
            a_d.append(items.designers)
        elif items.date_start.month == 5 and items.date_start.year == finplan_constants.CURRENT_YEAR:
            ma.append(items.draftsmen)
            #print(f"items.designers  {items.designers}")
            ma_d.append(items.designers)
        elif items.date_start.month == 6 and items.date_start.year == finplan_constants.CURRENT_YEAR:
            yun.append(items.draftsmen)
            #print(f"items.designers  {items.designers}")
            yun_d.append(items.designers)
        elif items.date_start.month == 7 and items.date_start.year == finplan_constants.CURRENT_YEAR:
            yu.append(items.draftsmen)
            #print(f"items.designers  {items.designers}")
            yu_d.append(items.designers)
        elif items.date_start.month == 8 and items.date_start.year == finplan_constants.CURRENT_YEAR:
            au.append(items.draftsmen)
            #print(f"items.designers  {items.designers}")
            au_d.append(items.designers)
        elif items.date_start.month == 9 and items.date_start.year == finplan_constants.CURRENT_YEAR:
            se.append(items.draftsmen)
            #print(f"items.designers  {items.designers}")
            se_d.append(items.designers)
        elif items.date_start.month == 10 and items.date_start.year == finplan_constants.CURRENT_YEAR:
            oc.append(items.draftsmen)
            #print(f"items.designers  {items.designers}")
            oc_d.append(items.designers)
        elif items.date_start.month == 11 and items.date_start.year == finplan_constants.CURRENT_YEAR:
            no.append(items.draftsmen)
            #print(f"items.designers  {items.designers}")
            no_d.append(items.designers)
        elif items.date_start.month == 12 and items.date_start.year == finplan_constants.CURRENT_YEAR:
            de.append(items.draftsmen)
            #print(f"items.designers  {items.designers}")
            de_d.append(items.designers)
    list_of_months = [y, f, m, a, ma, yun, yu, au, se, oc, no, de]
    list_of_months_designer = [y_d, f_d, m_d, a_d, ma_d, yun_d, yu_d, au_d, se_d, oc_d, no_d, de_d]
    list_of_months_names = ["y", "f", "m", "a", "ma", "yun", "yu", "au", "se", "oc", "no", "de"]
    ydraf = []
    ydes = []

    fdraf = []
    fdes = []

    mdraf = []
    mdes = []

    adraf = []
    ades = []

    madraf = []
    mades = []

    yundraf = []
    yundes = []

    yudraf = []
    yudes = []

    audraf = []
    audes = []

    sedraf = []
    sedes = []

    ocdraf = []
    ocdes = []

    nodraf = []
    nodes = []

    dedraf = []
    dedes = []

    dict_of_w_month = collections.OrderedDict(y=[ydraf, ydes,0,'Месяц 1'], f=[fdraf, fdes,1,'Месяц 2'], m=[mdraf, mdes,2,'Месяц 3'], a=[adraf, ades,3,'Месяц 4'],
                                              ma=[madraf, mades,4,'Месяц 5'], yun=[yundraf, yundes,5,'Месяц 6'], yu=[yudraf, yudes,6,'Месяц 7'],
                                              au=[audraf, audes,7,'Месяц 8'], se=[sedraf, sedes,8,'Месяц 9'], oc=[ocdraf, ocdes,9,'Месяц 10'],
                                              no=[nodraf, nodes,10,'Месяц 11'], de=[dedraf, dedes,11,'Месяц 12'])

    for month in dict_of_w_month.items():
        number = int((month[1][2]))  # Порядковый номер словаря
        name_s = (month[1][3])  # Имя столбца
        result_1 = list_of_months[number]
        result_2 = list_of_months_designer[number]
        draftmens = get_sum_of_list(result_1)
        designers = get_sum_of_list(result_2)
        #print(result_1)
        #print(result_2)
        dict_of_workers.append([name_s,draftmens,designers])
        #print(dict_of_workers)

    return dict_of_workers



def customer_flow():
    """
    January – Ja – Jan.
    February – Fe – Feb.
    March – Ma – Mar.
    April – Ap – Apr.
    May – May – May
    June – June – Jun.
    July – July – Jul.
    August – Au – Aug.
    September – Sept – Sep.
    October – Oc – Oct.
    November – No – Nov.
    December – De – Dec.

    Формирует дата фрейм с заявками из списка данных из класса class AdvertisingGeneratesLeads:
    @return: data frame с заказами инспирированными рекламной кампанией
    @rtype:
    """

    ja_add = AdvertisingGeneratesLeads(budget=finplan_constants.ADV_JAN,
                                       conversion=finplan_constants.CONVERSION_TO_CUSTOMER,
                                       cost_of_visiting_site=finplan_constants.COST_ONE_LID,
                                       date_start=date(finplan_constants.CURRENT_YEAR, 1, 5))
    fe_add = AdvertisingGeneratesLeads(budget=finplan_constants.ADV_FE,
                                       conversion=finplan_constants.CONVERSION_TO_CUSTOMER,
                                       cost_of_visiting_site=finplan_constants.COST_ONE_LID,
                                       date_start=date(finplan_constants.CURRENT_YEAR, 2, 5))
    ma_add = AdvertisingGeneratesLeads(budget=finplan_constants.ADV_MA,
                                       conversion=finplan_constants.CONVERSION_TO_CUSTOMER,
                                       cost_of_visiting_site=finplan_constants.COST_ONE_LID,
                                       date_start=date(finplan_constants.CURRENT_YEAR, 3, 5))
    ap_add = AdvertisingGeneratesLeads(budget=finplan_constants.ADV_AP,
                                       conversion=finplan_constants.CONVERSION_TO_CUSTOMER,
                                       cost_of_visiting_site=finplan_constants.COST_ONE_LID,
                                       date_start=date(finplan_constants.CURRENT_YEAR, 4, 5))
    may_add = AdvertisingGeneratesLeads(budget=finplan_constants.ADV_MAY,
                                        conversion=finplan_constants.CONVERSION_TO_CUSTOMER,
                                        cost_of_visiting_site=finplan_constants.COST_ONE_LID,
                                        date_start=date(finplan_constants.CURRENT_YEAR, 5, 5))
    jun_add = AdvertisingGeneratesLeads(budget=finplan_constants.ADV_JU,
                                        conversion=finplan_constants.CONVERSION_TO_CUSTOMER,
                                        cost_of_visiting_site=finplan_constants.COST_ONE_LID,
                                        date_start=date(finplan_constants.CURRENT_YEAR, 6, 5))
    jul_add = AdvertisingGeneratesLeads(budget=finplan_constants.ADV_JUL,
                                        conversion=finplan_constants.CONVERSION_TO_CUSTOMER,
                                        cost_of_visiting_site=finplan_constants.COST_ONE_LID,
                                        date_start=date(finplan_constants.CURRENT_YEAR, 7, 5))
    aug_add = AdvertisingGeneratesLeads(budget=finplan_constants.ADV_AU,
                                        conversion=finplan_constants.CONVERSION_TO_CUSTOMER,
                                        cost_of_visiting_site=finplan_constants.COST_ONE_LID,
                                        date_start=date(finplan_constants.CURRENT_YEAR, 8, 5))
    sep_add = AdvertisingGeneratesLeads(budget=finplan_constants.ADV_SE,
                                        conversion=finplan_constants.CONVERSION_TO_CUSTOMER,
                                        cost_of_visiting_site=finplan_constants.COST_ONE_LID,
                                        date_start=date(finplan_constants.CURRENT_YEAR, 9, 5))
    oc_add = AdvertisingGeneratesLeads(budget=finplan_constants.ADV_OC,
                                       conversion=finplan_constants.CONVERSION_TO_CUSTOMER,
                                       cost_of_visiting_site=finplan_constants.COST_ONE_LID,
                                       date_start=date(finplan_constants.CURRENT_YEAR, 10, 5))
    no_add = AdvertisingGeneratesLeads(budget=finplan_constants.ADV_NO,
                                       conversion=finplan_constants.CONVERSION_TO_CUSTOMER,
                                       cost_of_visiting_site=finplan_constants.COST_ONE_LID,
                                       date_start=date(finplan_constants.CURRENT_YEAR, 11, 5))
    de_add = AdvertisingGeneratesLeads(budget=finplan_constants.ADV_DE,
                                       conversion=finplan_constants.CONVERSION_TO_CUSTOMER,
                                       cost_of_visiting_site=finplan_constants.COST_ONE_LID,
                                       date_start=date(finplan_constants.CURRENT_YEAR, 12, 5))
    ja_start = (ja_add.make_calendar_of_lids()[0])
    ja_end = (ja_add.make_calendar_of_lids()[1])  # ЯНВАРЬ
    ja_lids = (ja_add.make_calendar_of_lids()[2])

    fe_start = (fe_add.make_calendar_of_lids()[0])
    fe_end = (fe_add.make_calendar_of_lids()[1])  # ФЕВРАЛЬ
    fe_lids = (fe_add.make_calendar_of_lids()[2])

    ma_start = (ma_add.make_calendar_of_lids()[0])
    ma_end = (ma_add.make_calendar_of_lids()[1])  # МАРТ
    ma_lids = (ma_add.make_calendar_of_lids()[2])

    ap_start = (ap_add.make_calendar_of_lids()[0])
    ap_end = (ap_add.make_calendar_of_lids()[1])  # АПРЕЛЬ
    ap_lids = (ap_add.make_calendar_of_lids()[2])

    may_start = (may_add.make_calendar_of_lids()[0])
    may_end = (may_add.make_calendar_of_lids()[1])  # МАЙ
    may_lids = (may_add.make_calendar_of_lids()[2])

    jun_start = (jun_add.make_calendar_of_lids()[0])
    jun_end = (jun_add.make_calendar_of_lids()[1])  # ИЮНЬ
    jun_lids = (jun_add.make_calendar_of_lids()[2])

    jul_start = (jul_add.make_calendar_of_lids()[0])
    jul_end = (jul_add.make_calendar_of_lids()[1])  # ИЮЛЬ
    jul_lids = (jul_add.make_calendar_of_lids()[2])

    aug_start = (aug_add.make_calendar_of_lids()[0])
    aug_end = (aug_add.make_calendar_of_lids()[1])  # АВГУСТ
    aug_lids = (aug_add.make_calendar_of_lids()[2])

    sep_start = (sep_add.make_calendar_of_lids()[0])
    sep_end = (sep_add.make_calendar_of_lids()[1])  # СЕНТЯБРЬ
    sep_lids = (sep_add.make_calendar_of_lids()[2])

    oc_start = (oc_add.make_calendar_of_lids()[0])
    oc_end = (oc_add.make_calendar_of_lids()[1])  # ОКТЯБРЬ
    oc_lids = (oc_add.make_calendar_of_lids()[2])

    no_start = (no_add.make_calendar_of_lids()[0])
    no_end = (no_add.make_calendar_of_lids()[1])  # НОЯБРЬ
    no_lids = (no_add.make_calendar_of_lids()[2])

    de_start = (de_add.make_calendar_of_lids()[0])
    de_end = (de_add.make_calendar_of_lids()[1])  # ДЕКАБРЬ
    de_lids = (de_add.make_calendar_of_lids()[2])
    list_of_datasets = []

    contract_dataset_ja = contract_dataset_generator(numbers=int(ja_lids),
                                                     start=str(
                                                         ja_start.day) + "." + str(ja_start.month) + "." + str(
                                                         ja_start.year),
                                                     end=str(ja_end.day) + "." + str(ja_end.month) + "." + str(
                                                         ja_end.year))
    #print(f"contract_dataset_ja !!! {contract_dataset_ja}")
    list_of_datasets.append(contract_dataset_ja)
    contract_dataset_fe = contract_dataset_generator(numbers=int(fe_lids),
                                                     start=str(
                                                         fe_start.day) + "." + str(fe_start.month) + "." + str(
                                                         fe_start.year),
                                                     end=str(fe_end.day) + "." + str(fe_end.month) + "." + str(
                                                         fe_end.year))
    list_of_datasets.append(contract_dataset_fe)

    contract_dataset_ma = contract_dataset_generator(numbers=int(ma_lids),
                                                     start=str(
                                                         ma_start.day) + "." + str(ma_start.month) + "." + str(
                                                         ma_start.year),
                                                     end=str(ma_end.day) + "." + str(ma_end.month) + "." + str(
                                                         ma_end.year))
    list_of_datasets.append(contract_dataset_ma)

    contract_dataset_ap = contract_dataset_generator(numbers=int(ap_lids),
                                                     start=str(
                                                         ap_start.day) + "." + str(ap_start.month) + "." + str(
                                                         ap_start.year),
                                                     end=str(ap_end.day) + "." + str(ap_end.month) + "." + str(
                                                         ap_end.year))
    list_of_datasets.append(contract_dataset_ap)

    contract_dataset_may = contract_dataset_generator(numbers=int(may_lids),
                                                      start=str(
                                                          may_start.day) + "." + str(may_start.month) + "." + str(
                                                          may_start.year),
                                                      end=str(may_end.day) + "." + str(may_end.month) + "." + str(
                                                          may_end.year))
    list_of_datasets.append(contract_dataset_may)

    contract_dataset_jun = contract_dataset_generator(numbers=int(jun_lids),
                                                      start=str(
                                                          jun_start.day) + "." + str(jun_start.month) + "." + str(
                                                          jun_start.year),
                                                      end=str(jun_end.day) + "." + str(jun_end.month) + "." + str(
                                                          jun_end.year))
    list_of_datasets.append(contract_dataset_jun)
    contract_dataset_jul = contract_dataset_generator(numbers=int(jul_lids),
                                                      start=str(
                                                          jul_start.day) + "." + str(jul_start.month) + "." + str(
                                                          jul_start.year),
                                                      end=str(jul_end.day) + "." + str(jul_end.month) + "." + str(
                                                          jul_end.year))
    list_of_datasets.append(contract_dataset_jul)
    contract_dataset_aug = contract_dataset_generator(numbers=int(aug_lids),
                                                      start=str(
                                                          aug_start.day) + "." + str(aug_start.month) + "." + str(
                                                          aug_start.year),
                                                      end=str(aug_end.day) + "." + str(aug_end.month) + "." + str(
                                                          aug_end.year))
    list_of_datasets.append(contract_dataset_aug)

    contract_dataset_sep = contract_dataset_generator(numbers=int(sep_lids),
                                                      start=str(
                                                          sep_start.day) + "." + str(sep_start.month) + "." + str(
                                                          sep_start.year),
                                                      end=str(sep_end.day) + "." + str(sep_end.month) + "." + str(
                                                          sep_end.year))
    list_of_datasets.append(contract_dataset_sep)
    contract_dataset_oc = contract_dataset_generator(numbers=int(oc_lids),
                                                     start=str(
                                                         oc_start.day) + "." + str(oc_start.month) + "." + str(
                                                         oc_start.year),
                                                     end=str(oc_end.day) + "." + str(oc_end.month) + "." + str(
                                                         oc_end.year))
    list_of_datasets.append(contract_dataset_oc)
    contract_dataset_no = contract_dataset_generator(numbers=int(no_lids),
                                                     start=str(
                                                         no_start.day) + "." + str(no_start.month) + "." + str(
                                                         no_start.year),
                                                     end=str(no_end.day) + "." + str(no_end.month) + "." + str(
                                                         no_end.year))
    list_of_datasets.append(contract_dataset_no)
    contract_dataset_de = contract_dataset_generator(numbers=int(de_lids),
                                                     start=str(
                                                         de_start.day) + "." + str(de_start.month) + "." + str(
                                                         de_start.year),
                                                     end=str(de_end.day) + "." + str(de_end.month) + "." + str(
                                                         de_end.year))
    list_of_datasets.append(contract_dataset_de)
    # Поток заказов не связанный с рекламой: Сайт, инстаграм, рекомендации

    contract_dataset_default = contract_dataset_generator(numbers=15,
                                                          start=f"01.01.{finplan_constants.CURRENT_YEAR}",
                                                          end=f"30.12.{finplan_constants.CURRENT_YEAR}")
    #print(f"715: {contract_dataset_default}")
    result = (from_data_set_to_list_pp_instance(contract_dataset_default))
    add_list_of_workers_to_fp(result)
    #print(contract_dataset_default)
    return contract_dataset_default  # ok


if __name__ == '__main__':
    # Создает фин.план на год
    data_set = make_finplan(2024)
    # Записывает фин.план в файл
    data_set.to_excel('XLSX/fin_plan_2024_2.xlsx', sheet_name=f'2024_Norma_profit_{ProjectPrice.PROFIT_NORM_PER_M}')

    # todo Подсчет кол-ва чертёжников и дизайнеров задействованных в процессе на каждый месяц!
    # todo Разобраться с очисткой дата фрейма
    # todo Посчитать ежегодный налог с прибыли и с комплектации
    # todo Сделать удобный подсчет стоимости проекта и создание КП в новом телеграм боте
    # todo Для разных сценариев загружать один и тот же сохраненый дата фрейм с данными
    # todo Альтернативный подсчет работников сделать
    # todo Скорректировать расчет дизайнеров и чертёжников, если это планировка или фор-проект
    # todo Вычесть из общей прибыли расходы на Арт-директоров
    # todo Объектов 170. Почему считает 115
