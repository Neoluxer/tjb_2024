import pandas as pd

df = pd.read_excel('vipiska.xls')
from datetime import datetime
pd.set_option('display.max_columns', None)
# print(df.to_string())
debet_df = df[(df['type'] == 'Д') & (df['kor'].str.contains('Кандалов Владимир Анатольевич'))]
kredit_df = df[(df['kor'].str.contains('Кандалов Владимир Анатольевич')) & (df['type'] == 'К')]  # Поступления


def loan_proceeds(date_start: datetime):
    """
    Поступления по договору займа с определенного года
    """
    data_k = df[(df['kor'].str.contains('Кандалов Владимир Анатольевич')) & (df['type'] == 'К') & (
        df['description'].str.contains('беспроцентного займа')) & ((df['date'].str[6:]) == str(date_start.year))]
    return data_k

def debt_repayment(date_start: datetime):
    """
    Возврат по договору займа
    """
    data_k = df[(df['kor'].str.contains('Кандалов Владимир Анатольевич')) & (df['type'] == 'Д') & (
        df['description'].str.contains('беспроцентного')) & ((df['date'].str[6:]) == str(date_start.year))]
    return data_k


if __name__ == '__main__':
    print(f'{sum(debet_df["summa"])} :общие расходы на контрагента Кандалова с 01.01.2020 ')
    print(f'{sum(kredit_df["summa"])} :общие доходы от контрагента Кандалова с 01.01.2020 ')
    text_loan_2023 = (loan_proceeds(datetime(year=2023, month=1, day=1)))
    text_loan_2022 = (loan_proceeds(datetime(year=2022, month=1, day=1)))
    text_loan_2023.to_excel('result.xlsx')
    text_loan_2022.to_excel('result2.xlsx')
    text_return_2023 = debt_repayment(datetime(year=2022, month=1, day=1))
    text_return_2023.to_excel('return_2023.xlsx')
