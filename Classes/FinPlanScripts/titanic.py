import pandas as pd

titanic = pd.read_csv("C:\\Users\\User\\PycharmProjects\\tjb_2024\\Classes\\FinPlanScripts\\XLSX\\titanic.csv")
print(titanic.head())

"""
https://pandas.pydata.org/docs/getting_started/intro_tutorials/06_calculate_statistics.html
"""
# Каков средний возраст пассажиров Титаника?
# Формула: (сумма значений) / общие значения

"""
Средняя зарплата и медианная зарплата — это две разные величины измерения доходов. 
Средняя зарплата высчитывается как сумма всех зарплат, поделëнная на количество людей, зарабатывающих эти зарплаты.
А медианная — это такая зарплата, когда половина людей зарабатывает меньше этой суммы, а другая половина — больше
"""

print(titanic["Age"].mean())
# Каков средний возраст и стоимость билетов пассажиров Титаника?
print(titanic[["Age", "Fare"]].median())
print(titanic[["Age", "Fare"]].mean())

# sum общая сумма
# count количество

agg = titanic.agg(
    {
        "Age": ["min", "max", "median", "skew", "sum", "count"],
        "Fare": ["min", "max", "median", "mean"],
    }
)

print(agg)

sum_age = titanic.agg({"Age": ["sum"]})
# Достал сумму значений
print((sum_age.values[0][0]))

import random

for i in range(5):

    # Any number can be used in place of '11'.
    random.seed(16)

    # Generated random number will be between 1 to 1000.
    print(random.randint(1, 1000))
