SHEETS = 10  # Количество неизменных листов в проекте. Коэффициент сложности относится к ним
PROFIT_NORM_PER_M = 200_000  # Норма прибыли в месяц
OVERHEAD_PER_M = 9233 + 3120  # Расходы без УСН налога (6%) и без Аренды офиса
WAGE_OF_DESIGNER = 1000  # Гонорар дизайнера за квадрат
WAGE_OF_DRAFTSMEN = 500  # Гонорар чертёжника за квадрат
WORKING_HOURS = 4  # Кол-во рабочих часов в рабочем дне
DRAFTSMENS = 2
DESIGNERS = 2
MIDDLE_ROOM = 15
NORM_AREA_FOR_DESIGNER = 50
NORM_AREA_FOR_DRAFTSMEN = 100
FULL_PROJECT_PAYMENTS = [0.085, 0.32, 0.415, 0.18]
"""------------------------------------------------"""
CURRENT_YEAR = 2024  # Текущий год для рекламной кампании
#ADV_JAN = 25_000  # Расход на рекламу в январе
#ADV_FE = 50_000  # Расход на рекламу в феврале
#ADV_MA = 50_000  # Расход на рекламу в марте34
#ADV_AP = 75_000 # Расход на рекламу в апреле
#ADV_MAY = 75_000  # Расход на рекламу в мае
#ADV_JU = 75_000  # Расход на рекламу в июне
#ADV_JUL = 75_000  # Расход на рекламу в июле
#ADV_AU = 75_000  # Расход на рекламу в августе
#ADV_SE = 75_000  # Расход на рекламу в сентябре
#ADV_OC = 75_000  # Расход на рекламу в октябре
#ADV_NO = 75_000  # Расход на рекламу в ноябре
#ADV_DE = 75_000  # Расход на рекламу в декабре
COST_ONE_LID = 250  # Стоимость одного лида
CONVERSION_TO_CUSTOMER = 0.02  # Конверсия лида в покупателя
#ALL_ADV_EXPENSES = ADV_JAN + ADV_FE + ADV_MA + ADV_AP + ADV_MA + ADV_JU + ADV_JUL + ADV_AU + ADV_SE + ADV_OC + \
                   #ADV_NO + ADV_DE

"""------------------------------------------------"""
ODINTSOVO_AREA = 111
COMPLECTATION_PROFIT_ODINTSOVO = 689_946
RYAZANOVA_AREA = 350
COMPLECTATION_PROFIT_RYAZANOVA = 1_562_400
MEDIUM_COMPLECTATION_PROCENT = (0.094 + 0.072) / 2
ALL_BUDJET_RYAZANOVA = 20_000_000 + (689_946 * 10)
BUDJET_PER_METER_RYASANOVA = 76_855
ALL_BUDJET_ODINTSOVO_PER_METER = 63_564
MEDIUM_COMPLECTATION_BUDJET = (BUDJET_PER_METER_RYASANOVA + ALL_BUDJET_ODINTSOVO_PER_METER) / 2
# 5827 Столько зарабатываем с квадратного метра комплектации:
COMPL_MED_PROFIT = (MEDIUM_COMPLECTATION_BUDJET * MEDIUM_COMPLECTATION_PROCENT)
POTENTIAL_PROFIT_BUILDING_PER_METER = 20_000/10
