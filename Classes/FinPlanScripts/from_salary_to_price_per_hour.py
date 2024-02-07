WORKING_HOURS = 8  # Кол-во рабочих часов в рабочем дне


def validator(value):
    """
    Проверка на целое число больше нуля
    """
    if isinstance(value, int):
        if value > 0:
            return True
        else:
            return False
    else:
        return False


def salary_to_week(value: int) -> float:
    """
    Вычисление дохода в неделю по доходу в месяц
    """
    assert validator(value), 'Неверно введен доход для salary_to_week() '
    return value / 4


def salary_to_working_days(value: int) -> float:
    """
    Вычисление дохода в день по доходу в месяц
    """
    assert validator(value), 'Неверно введен доход для salary_to_working_days()'
    return value / 20.67


def salary_to_working_hours(value: int) -> float:
    """
    Вычисление дохода в час по доходу в месяц
    """
    assert validator(value), 'Неверно введен доход для salary_to_working_hours() '
    return salary_to_working_days(value) / WORKING_HOURS


if __name__ == '__main__':
    print('При заработной плате 100 000 рублей:')
    print(f'Стоимость рабочей недели: {(salary_to_week(100_000))} рублей')
    print(f'Стоимость рабочего дня: {round(salary_to_working_days(100_000), 1)} рублей')
    print(f'Стоимость рабочего часа: {round(salary_to_working_hours(100_000), 1)}'
          f' рублей. Рабочих часов в день: {WORKING_HOURS}')
