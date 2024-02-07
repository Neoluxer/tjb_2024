"""
Количество новых визитов
Конверсия в потенциального клиента из визита
Количество новых потенциальных клиентов
% оттока клиентов за месяц
Клиентская база
Конверсия из потенциального клиента в оплату
% покупок накопленной базы
"""
from datetime import date, timedelta


class AdvertisingGeneratesLeads:
    def __init__(self, budget, conversion, cost_of_visiting_site, date_start: date):
        self.budget = budget
        self.conversion = conversion
        self.cost_of_visiting_site = cost_of_visiting_site
        self.date_start = date_start

    def make_lid(self):
        return self.budget / self.cost_of_visiting_site * self.conversion

    def make_calendar_of_lids(self):
        """
        Распределяем равномерно лидов на пол года от даты рекламы
        @return: Начальная дата, конечная дата, число заявок
        @rtype:
        """
        start_date = self.date_start
        delta = timedelta(days=(6 * 30 ))
        return [start_date,start_date + delta,self.make_lid()]


if __name__ == '__main__':
    new_add = AdvertisingGeneratesLeads(budget=25_000, conversion=0.1, cost_of_visiting_site=250,
                                        date_start=date(2024, 1, 30))
    print(new_add.make_lid())
    print(new_add.make_calendar_of_lids())
