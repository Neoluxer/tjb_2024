import math
from datetime import datetime, timedelta

from Classes.FinPlanScripts.finplan_constants import *

now_date = datetime.now()
dp_list = ['обмеры',
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
           'cхема сан.тех.приборов'
           ]

dp_c_list = ['обмеры',
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
             'комплектация',

             ]
fp_list = ['обмеры',
           'электрика',
           'планировка',
           'кладочный план',
           'демонтаж',
           'план ТП',
           'план пола',
           'план потолка',
           'обложка', ]


class ProjectPrice:
    time_periods_dict = {"pre_design_work": 17}  # Время на предпроектную работу

    # ФОНД ОПЛАТЫ ТРУДА В МЕСЯЦ:

    #: Константа сколько плачу за бухгалтерское обслуживание в месяц
    ACCOUNTANT_SALARY = 5_000
    ART_DIRECTOR_SALARY = 60_000  # Константа зарплата арт-директора в месяц
    AUTHORS_SUPERVISION_SALARY = 15_000  # Константа зарплата авторского надзора в месяц
    DIRECTOR_SALARY = 100_000  # Константа зарплата директора в месяц
    SUPPLIER_SALARY = 60_000  # Константа зарплата комплектатора в месяц
    WAGE_OF_DESIGNER = 1000  # Константа дизайнеру за квадратный метр
    WAGE_OF_DRAFTSMEN = 500  # Константа чертёжнику за квадратный метр Альбома чертежей
    WAGE_OF_DRAFTSMEN_FP = 200  # Константа чертёжнику за квадратный метр Фор-Проекта
    WAGE_OF_DRAFTSMEN_P = 150  # Константа чертёжнику за квадратный метр Планировки

    # Налоги:
    USN_INCOME = 0.06
    USN_PROFIT = 0.15
    USN_MINIMUM = 0.01

    """
    Из суммы налога при УСН «Доходы» можно вычесть (п. 3.1 ст. 346.21 НК РФ):
    Обязательные страховые взносы за работников.
    Оплату больничных за счет работодателя.
    Взносы по личному страхованию в пользу работников.
    Страховые взносы ИП за себя.
    """

    # Накладные расходы
    #: Price for 4 copies of printing docs
    SHEET_PRINTING_COST = 15 * 4
    TO_THE_PIGGY_BANK = 0.3  # Откладываем в запас и на развитие

    # Производительность в квадратных метрах в месяц на работника

    DRAFTSMEN_PERFORMANCE = 350 / 2  # Чертёжник
    DESIGNER_PERFORMANCE = 22 * 5  # Дизайнер
    ART_DIRECTOR_PERFORMANCE = 22 * 5 * 4  # Арт-директор
    AUTHORS_SUPERVISION_PERFORMANCE = 350  # Авторский надзор
    SUPPLIER_PERFORMANCE = 300  # Комплектатор
    number_of_visualizations_per_day = 7

    # Комплектация

    furniture_and_decoration_costs = 200_000  # Расходы на мебель, оборудование и отделку на квадратный метр
    # todo Проверить эти цифры
    percentage_of_supply_revenue = 0.05  # Средний процент заработка с комплектации
    supply_conversion = 0.8  # Процент позиций, с которых мы зарабатываем на комплектации

    # Прочие константы
    SHEETS = 10  # Количество неизменных листов в проекте. Коэффициент сложности относится к ним
    PROFIT_NORM_PER_M = 200_000  # Норма прибыли в месяц

    OVERHEAD_PER_M = 13_939 + 341  # Накладные расходы без УСН налога (6%) и без Аренды офиса
    wage_of_designer = 1000  # Гонорар дизайнера за квадрат
    wage_of_draftsmen = 500  # Гонорар чертёжника за квадрат
    WORKING_HOURS = 4  # Кол-во рабочих часов в рабочем дне
    DRAFTSMAN = 1  # Количество чертёжников по умолчанию на объект
    DESIGNERS = 1  # Количество дизайнеров по умолчанию на объект
    MIDDLE_ROOM = 15  # Средний размер комнаты
    NORM_AREA_FOR_DESIGNER = 150  # Какую площадь мы выдаем дизайнеру в работу по одному объекту проектирования
    FULL_PROJECT_PAYMENTS = [0.085, 0.32, 0.415, 0.18]  # Платежи по полному дизайн проекту в процентном соотношении

    def __init__(self, square, spaces, typeof: int, content: list, designers=DESIGNERS, draftsmen=DRAFTSMENS,
                 profit_norm_perm: int = PROFIT_NORM_PER_M, wage_of_designer: int = WAGE_OF_DESIGNER,
                 wage_of_draftsmen: int = WAGE_OF_DRAFTSMEN,
                 time_of_one_vis: int = 3, time_of_vis: int = 1, time_of_blueprint: int = 1, overh: int = None,
                 date_start: datetime = '2025-01-19'):
        """
        @type time_of_vis: int
            Время, которое потребуется на создание визуализаций
        """
        self.overh = overh
        self.date_start = date_start  # Дата начала работы над проектом
        self.timeOfBlueprint = time_of_blueprint
        self.time_of_vis = time_of_vis
        self.square = square  # Площадь
        self.typeof = typeof  # Тип помещения
        self.content = content  # Состав проекта
        self.designers = designers  # Количество дизайнеров
        self.draftsmen = draftsmen  # Количество чертёжников
        self.spaces = spaces  # Количество комнат
        self.time_of_one_vis = time_of_one_vis
        self.sheets = 10  # Количество неизменных листов в проекте. Коэффициент сложности относится к ним
        self.profitNormPerM = profit_norm_perm  # Норма прибыли в месяц
        self.overheadPerM = 13_939 + 341  # Единый налоговый платёж и взносы на обязательное страхование от несчастных
        # случаев без УСН налога (6%) и без Аренды офиса
        self.wageOfDesigner = wage_of_designer  # Гонорар дизайнера за квадрат
        self.wageOfDraftsmen = wage_of_draftsmen  # Гонорар чертёжника за квадрат
        self.base_price = 3500

    def calculate_price_per_meter(self):
        """Подсчитывает цену за м.кв."""

        fot = (self.square * (self.wageOfDesigner + self.wageOfDraftsmen + self.WAGE_OF_DRAFTSMEN_FP))
        time_of_making_project = (
                                         self.time_of_visualization() + self.time_of_blueprints() + 10) / 30  # Время в месяцах на проект
        target_profit = self.profitNormPerM * time_of_making_project  # Например 300_000
        all_fot = fot * self.project_parts()
        target_coast = target_profit + all_fot
        result = (target_coast / (self.square * time_of_making_project)) * self.project_parts()
        self.designers = self.square / self.NORM_AREA_FOR_DESIGNER
        # print(f'Площадь: {self.square}')
        # print(f'Фонд оплаты труда: {fot} за полный проект')
        # print(f'Время в месяцах на проект: {time_of_making_project}')
        # print (f'Отдаем исполнителям {all_fot} из {self.square*3500}')
        # print(f'target profit за всё время выполнения проекта = {target_profit}')
        # print(f'target cost: {target_coast}')
        # print(f'result = {result}')
        if len(self.content) < 10 or self.content == ['фор-проект']:
            result = self.base_price * self.project_parts()
        return result

    def time_of_visualization(self):
        """
        @return: Расчет времени на визуализацию
        """
        print(self.content[0])
        # Округляем в большую сторону:

        if self.content[0] == 'фор-проект':
            print("!!!!!!!!!!!!!!!!!!")
            self.time_of_vis = 1
        elif "визуализация" in self.content:
            self.time_of_vis = (self.spaces * self.time_of_one_vis) / self.designers
        elif "полный дизайн проект" in self.content:
            self.time_of_vis = (self.spaces * self.time_of_one_vis) / self.designers
        elif "проект с авторским надзором" in self.content:
            self.time_of_vis = (self.spaces * self.time_of_one_vis) / self.designers
        elif "проект с комплектацией" in self.content:
            self.time_of_vis = ((self.spaces * self.time_of_one_vis) / self.designers) + self.spaces

        else:
            self.time_of_vis = 1

        return self.time_of_vis

    def time_of_blueprints(self):
        """
        @return: Расчет времени на чертежи исходя из количества листов
        """
        if self.content == ['проект с комплектацией'] or self.content == [
            'проект с авторским надзором'] or self.content == [
            'проект со схематичной визуализацией'] or self.content == ['полный дизайн проект']:
            self.timeOfBlueprint = math.ceil(
                (self.sheets + self.spaces + self.SHEETS) / self.draftsmen)  # Округляем в большую сторону

        else:
            if 'развертки' not in self.content:
                self.timeOfBlueprint = len(self.content) + 1
            else:
                self.timeOfBlueprint = len(self.content) - 1 + self.spaces

        return self.timeOfBlueprint

    def full_project_calendar_second_pay(self):
        """
        @return: Расчет даты второго платежа для полного дизайн-проекта
        """
        date_time_obj = datetime.strptime(str(self.date_start), '%Y-%m-%d')
        pre_project_delta = timedelta(days=17)
        return date_time_obj + pre_project_delta

    def full_project_calendar_third_pay(self):
        """
        @return: Расчет даты третьего платежа для полного дизайн-проекта
        """
        second_pay_date = self.full_project_calendar_second_pay()
        delta = timedelta(days=self.time_of_visualization())
        return second_pay_date + delta

    def full_project_calendar_final_pay(self):
        """
        @return: Расчет даты последнего платежа для полного дизайн-проекта
        """
        third_pay_date = self.full_project_calendar_third_pay()
        delta = timedelta(days=self.time_of_blueprints())
        return third_pay_date + delta

    def complectation_calendar_first_pay(self):
        delta = timedelta(days=self.time_of_visualization() + self.time_of_blueprints() + 10)
        date_unformated = datetime.strptime(str(self.date_start), '%Y-%m-%d') + delta
        date_formated = str(f"{date_unformated.year}-{date_unformated.month}")
        return [date_formated]

    def complectation_calendar_second_pay(self):
        delta = timedelta(days=73)
        date_unformated = datetime.strptime(str(self.date_start), '%Y-%m-%d') + \
                          timedelta(days=self.time_of_visualization() + self.time_of_blueprints() + 10) + delta
        date_formated = str(f"{date_unformated.year}-{date_unformated.month}")
        return [date_unformated, date_formated]

    def complectation_calendar_third_pay(self):
        delta = timedelta(days=73)
        date_unformated = self.complectation_calendar_second_pay()[0] + delta
        date_formated = str(f"{date_unformated.year}-{date_unformated.month}")
        return [date_unformated, date_formated]

    def complectation_calendar_fourth_pay(self):
        delta = timedelta(days=73)
        date_unformated = self.complectation_calendar_third_pay()[0] + delta
        date_formated = str(f"{date_unformated.year}-{date_unformated.month}")
        return [date_unformated, date_formated]

    def complectation_calendar_fifths_pay(self):
        delta = timedelta(days=73)
        date_unformated = self.complectation_calendar_fourth_pay()[0] + delta
        date_formated = str(f"{date_unformated.year}-{date_unformated.month}")
        return [date_formated]

    def full_project_payments_calendar(self):
        """
        @return: Создает календарь поступлений по платежам с суммами для полного дизайн-проекта
        """
        # todo Передавать дату старта
        # self.date_start = datetime.now().date()

        marker_complectation = "комплектация"

        calendar_2 = {
            self.complectation_calendar_first_pay()[0]: (int(self.additional_complectation_profit()) / 5),
            self.complectation_calendar_second_pay()[1]: (int(self.additional_complectation_profit()) / 5),
            self.complectation_calendar_third_pay()[1]: (int(self.additional_complectation_profit()) / 5),
            self.complectation_calendar_fourth_pay()[1]: (int(self.additional_complectation_profit()) / 5),
            self.complectation_calendar_fifths_pay()[0]: (int(self.additional_complectation_profit()) / 5)}

        try:
            calendar_1 = {str(self.date_start.year) + "-" + str(self.date_start.month): FULL_PROJECT_PAYMENTS[0]
                                                                                        * self.overhead() * self.square,
                          str(self.full_project_calendar_second_pay().year) +
                          "-" + str(self.full_project_calendar_second_pay().month): float(
                              FULL_PROJECT_PAYMENTS[1] * self.overhead() * self.square),
                          str(self.full_project_calendar_third_pay().date().year) +
                          "-" + str(self.full_project_calendar_third_pay().date().month): float(
                              FULL_PROJECT_PAYMENTS[2] * self.overhead() * self.square),
                          str(self.full_project_calendar_final_pay().date().year) +
                          "-" + str(self.full_project_calendar_final_pay().date().month): float(
                              FULL_PROJECT_PAYMENTS[3] * self.overhead() * self.square),
                          }
            if marker_complectation in self.content:
                new_dict = self.sum_of_dicts(calendar_1, calendar_2)
                return new_dict
            else:
                return calendar_1

        except:
            self.date_start = datetime.now().date()
            calendar_1 = {str(self.date_start.year) + "-" + str(self.date_start.month): FULL_PROJECT_PAYMENTS[0]
                                                                                        * self.overhead() * self.square,
                          str(self.full_project_calendar_second_pay().year) +
                          "-" + str(self.full_project_calendar_second_pay().month): float(
                              FULL_PROJECT_PAYMENTS[1] * self.overhead() * self.square),
                          str(self.full_project_calendar_third_pay().date().year) +
                          "-" + str(self.full_project_calendar_third_pay().date().month): float(
                              FULL_PROJECT_PAYMENTS[2] * self.overhead() * self.square),
                          str(self.full_project_calendar_final_pay().date().year) +
                          "-" + str(self.full_project_calendar_final_pay().date().month): float(
                              FULL_PROJECT_PAYMENTS[3] * self.overhead() * self.square)}
            if marker_complectation in self.content:
                new_dict = self.sum_of_dicts(calendar_1, calendar_2)
                return new_dict
            else:
                return calendar_1

    def project_parts(self):
        """
        @return: Возвращает процент от целого полного дизайн-проекта в зависимости от списка self.content
        """
        price = {'обмеры': 0.08,  # 0.015323
                 'электрика': 0.030647,
                 'планировка': 0.1,  # 0.04597
                 'кладочный план': 0.007378,
                 'демонтаж': 0.007378,
                 'план тёплого пола': 0.007378,
                 'план ТП': 0.007378,
                 'развертки': 0.122588,
                 'ведомость': 0.053916,
                 'план пола': 0.015323,
                 'план потолка': 0.030647,
                 'мебельные конструкции': 0.022701,
                 'визуализация': 0.615778,
                 'фор-проект': 0.3,  # 0.141884
                 'альбом планировочных решений': 0.085131,
                 'обложка': 0.001135,
                 'электрика освещение': 0.015323,
                 'электрика розетки': 0.015323,
                 'узлы потолка': 0.005675,
                 'примечание': 0.00135,
                 'ведомость электроустановки': 0.00135,
                 'ведомость дверей': 0.00135,
                 'схема разверток стен': 0.00135,
                 'cхема сан.тех.приборов': 0.00135,
                 'комплектация': 0.3,
                 'авторский надзор': 0.5,
                 'схематичная визуализация': 1 - 0.5,
                 'полный дизайн проект': 1,
                 'проект со схематичной визуализацией': 1 - 0.5,
                 'проект с авторским надзором': 1.5,
                 'проект с комплектацией': 1.3,

                 }
        summa = 0
        try:
            for keys in self.content:
                if keys.lower() in price:
                    summa += float(price[keys.lower()])
                else:
                    continue
            return summa
        except Exception as e:
            print(e)
            print(f'content: {self.content}')
            return summa

    def additional_complectation_profit(self):
        marker_complectation = "комплектация"
        if marker_complectation in self.content:
            return COMPL_MED_PROFIT * self.square
        else:
            return 0

    def overhead(self):
        """
        @return: Цену за квадратный метр, исходя из параметров проекта и нормы прибыли
        @rtype:

        """

        fot = (self.square * self.wageOfDesigner) + (self.square * self.wageOfDraftsmen)

        norma_profit = (self.profitNormPerM * (self.time_of_visualization() / 30 + self.time_of_blueprints() / 30))
        self.overh = math.ceil(((
                                        self.overheadPerM * self.time_of_visualization() / 30 +
                                        self.time_of_blueprints() / 30)
                                + fot + norma_profit) / self.square)
        if self.overh > 100000:
            self.overh = 100000
        elif self.overh < 800:
            self.overh = 800
        return round(self.overh * self.project_parts(), 0)

    @classmethod
    def sum_of_dicts(self, d1, d2):
        """
        Суммирует данные из двух словарей
        @param d1:
        @type d1:
        @param d2:
        @type d2:
        @return: dict
        @rtype:
        """
        d = d1

        for key, value in d2.items():
            if key in d1:
                d[key] += value
            else:
                d.update({key: value})

        return d


if __name__ == '__main__':
    newInterior = ProjectPrice(square=100, spaces=15, typeof=1, content=fp_list,
                               designers=2,
                               draftsmen=2)

    t = newInterior.time_of_visualization()
    r = newInterior.time_of_blueprints()
    o = newInterior.calculate_price_per_meter()
    p = newInterior.project_parts()

    print(f'Время на визуализацию: {t}\nВремя на чертежи: {r}\nОбщее время: {t + r}\nЦена за м.кв.: {o}\n'
          f'Часть проекта: {p}')

    # print()
    # print(f'Сегодня дата: {now_date.date()}')
    # print(f'Дата первого платежа: {newInterior.date_start}')
    # print(f'Дата второго платежа: {newInterior.full_project_calendar_second_pay().date()}')
    # print(f'Дата третьего платежа: {newInterior.full_project_calendar_third_pay().date()}')
    # print(f'Дата последнего платежа: {newInterior.full_project_calendar_final_pay().date()}')
    # print(f'Общее время на проект: {t + r + 15}')
    # print(
    #     f'Цена за квадратный метр: {newInterior.calculate_price_per_meter()} исходя из нормы прибыли {newInterior.profitNormPerM} '
    #     f'рублей в месяц')
    # print(f'Календарь платежей: {newInterior.full_project_payments_calendar()}')
    # print(f"Дата пятого платежа {newInterior.complectation_calendar_fifths_pay()}")
    # print(newInterior.complectation_calendar_first_pay())
    # d2 = newInterior.full_project_payments_calendar()
    # print(sum(d2.values()) / newInterior.square)
