# Не оптимизировать импорты и не менять их порядок

import os, django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dj_ac.settings")
os.environ.update({'DJANGO_ALLOW_ASYNC_UNSAFE': "true"})
django.setup()

import logging
from asgiref.sync import sync_to_async
from app_telegram.models import TGUser
from addprofit.models import AddProfits
from lids.models import Lids


logger = logging.getLogger(__name__)


import os.path
from num2words import num2words # Перевод чисел в слова
import openpyxl # Работа с файлами XLSX
from datetime import *
from tgbot.data import config
from tgbot.templates.contract_templates import base_text_from_8_to_11, shapka_dogovora
from russian_names import RussianNames # Библиотека русских имён и фамилий для тестирования и генерации.
import pymorphy2 # Морфологический анализ и склонения

morph = pymorphy2.MorphAnalyzer()
@sync_to_async()
class Contract:
    print("* class Contract")
    """
    Класс Contract используется для создания Договоров

    """

    def __str__(self):  # Магический дандр метод форматирования вывода print(p): Дело(Название=1, Сделано?=1)
        return f'Документ: {self.number} {self.date}\n' \
               f'   Заказчик: {self.customername}\n' \
               f'   Исполнитель: {self.executor}\n' \
               f'   Сумма: {self.summa} рублей \n' \
               f'   Основание: {self.name_of_services}\n'

    def __init__(self,
                 path: str = 'tgbot/HTML/',
                 prefix: int = 443,
                 customername: str = 'Иванов Иван Иванович',
                 customer_firm: str = 'ООО СУ «Астон» ',
                 customer_legal_basis: str = 'Устава предприятия',
                 customer_delegate: str = 'Иванова Екатерина Павловна',
                 executor: str = 'ООО "Неолюкс", ИНН 6658215373, КПП 231001001, 350010, г. Краснодар, ул. Зиповская,'
                                 ' д. 5, Телефон: +7 (978) 074-08-54 ',
                 name_of_services: str = 'Дизайн проект по Договору', units: str = 'кв.м.', quantity: int = 100,
                 price: int = 1250, square: int = 100,
                 nds: str = 'Без НДС', names: int = 3,
                 number: int = 553,
                 client_id: int = 0,
                 director: str = 'Кандалов В.А.', bookkeeper: str = 'Кандалов В.А.', mail: str = 'не указана',
                 adressofobject: str = 'не указан',
                 townobject: str = 'Краснодар', passportnumber: str = 'не указан',
                 issued: str = 'не указано', whenissued: str = 'не указано', placeofregistration: str = 'не указано',
                 telephonenum: str = 'не указан',
                 organization_name: str = 'не указан',
                 organization_full_name: str = 'не указан',
                 organization_adress: str = 'не указан',
                 organization_inn: str = 'не указан',
                 organization_kpp: str = 'не указан',
                 ogrn: str = 'не указан',
                 date_of_firm_registration: str = 'не указан',
                 okpo: str = 'не указан',
                 organization_rs: str = 'не указан',
                 bank_name: str = 'не указан',
                 bank_bik: str = 'не указан',
                 bank_ks: str = 'не указан',
                 ):
        # self.number = number  # Номер договора (достается из счетчика)
        self.pefix = prefix
        self.path = path
        self.customer_legal_basis = customer_legal_basis  # Основание, на котором действует представитель
        self.customer_firm = customer_firm  # Название организации
        self.customername = customername  # Заказчик (достается из словаря с заказчиками или из БД)
        self.customer_delegate = customer_delegate  # Представитель организации
        self.executor = executor  # Исполнитель
        self.name_of_services = name_of_services  # Наименование услуг
        self.units = units  # Еденицы измерения
        self.quantity = quantity  # Количество
        self.price = price  # Цена
        self.client_id = client_id  # Идентификатор клиента
        self.number = number  # Номер договора
        self.summa = '{0:.2f}'.format(float(self.price) * float(self.quantity))  # Сумма
        self.data = datetime.now()  # Дата счета
        self.nds = nds  # НДС
        self.names = names  # Номер договора (Нужно будет связать с бд. А пока со счетчиком)
        self.director = director  # ФИО директора
        self.bookkeeper = bookkeeper  # ФИО главного бухгалтера
        self.mail = mail  # Эл.почта клиента
        self.square = square  # Площадь проектирования
        self.adressofobject = adressofobject  # Адрес объекта
        self.townobject = townobject  # Город объекта
        self.passportnumber = passportnumber  # Номер паспорта заказчика
        self.issued = issued  # Кем выдан паспорт
        self.whenissued = whenissued  # Когда выдан паспорт
        self.placeofregistration = placeofregistration  # Место регистрации клиента (прописка)
        self.telephonenum = telephonenum  # Номер телефона
        self.date = datetime.today().strftime("%d.%m.%Y")  # Текущая дата
        self.profit = 120000  # норма прибыли в месяц
        self.timeforplan = int(int(self.square) / 14)  # время на планировку
        self.timeforviz = int(self.square / 7)  # время на визуализацию
        self.timeforblueprint = int(self.square / 7.14)  # время на чертежи
        self.NPd = int(self.profit / 30)  # норма прибыли в день
        self.NacladnieRashodiPerDay = 700 * 1  # Рублей в день накладные расходы

        self.Cena_Raschetnaya_Planirovki = (self.NPd * self.timeforplan) + (50 * self.square) + (
                self.NacladnieRashodiPerDay * self.timeforplan)
        self.Cena_Raschetnaya_Visualisation = (self.NPd * self.timeforviz) + (400 * self.square) + (
                self.NacladnieRashodiPerDay * self.timeforviz)
        self.Cena_Raschetnaya_Chertezhey = (self.NPd * self.timeforblueprint) + (200 * self.square) + (
                self.NacladnieRashodiPerDay * self.timeforblueprint)
        self.Obshaya_Raschetnaya_cena = self.Cena_Raschetnaya_Planirovki + self.Cena_Raschetnaya_Visualisation + \
                                        self.Cena_Raschetnaya_Chertezhey
        self.Odin_procent = self.Obshaya_Raschetnaya_cena / 100
        self.Proc_Plan = (self.Cena_Raschetnaya_Planirovki / self.Odin_procent)
        self.Proc_Viz = (self.Cena_Raschetnaya_Visualisation / self.Odin_procent)
        self.Proc_Chert = (self.Cena_Raschetnaya_Chertezhey / self.Odin_procent)
        self.Proc_Plan_round = round(self.Proc_Plan, 0)
        self.Proc_Viz_round = round(self.Proc_Viz, 0)
        self.Proc_Chert_round = round(self.Proc_Chert, 0)
        self.Perviy_platezh = (self.square * self.price * self.Proc_Plan_round / 200)
        self.Vtoroy_platezh = self.Perviy_platezh
        self.Tretiy_platezh = (self.square * self.price * self.Proc_Viz_round / 200)
        self.Chetvertiy_platezh = (self.square * self.price * self.Proc_Viz_round / 200)
        self.Pyatiy_platezh = (self.square * self.price * self.Proc_Chert_round / 200)
        self.Shestoy_platezh = (self.square * self.price * self.Proc_Chert_round / 200)
        self.Obshaya_summa_dogovora = self.square * self.price

        # Расчет для общего договора на 4 платежа
        self.First_pay = int(self.Perviy_platezh)
        self.Second_pay = int(self.Vtoroy_platezh + self.Tretiy_platezh)
        self.Third_pay = int(self.Chetvertiy_platezh + self.Pyatiy_platezh)
        self.Fourth_pay = int(self.Shestoy_platezh)
        self.First_pay_word = num2words(str(self.First_pay), lang='ru')
        self.Second_pay_word = num2words(str(self.Second_pay), lang='ru')
        self.Third_pay_word = num2words(str(self.Third_pay), lang='ru')
        self.Fourth_pay_word = num2words(str(self.Fourth_pay), lang='ru')

        self.Obshaya_summa_dogovora_word = num2words(str(self.Obshaya_summa_dogovora), lang='ru')
        self.M_word = num2words(self.price, lang='ru')
        self.Obshiy_srok = int(self.timeforblueprint + self.timeforviz + self.timeforplan)

        self.organization_name = self.customer_firm  # Название организации заказчика
        self.organization_full_name = organization_full_name  # Полное наименование организации заказчика
        self.organization_adress = organization_adress  # Юр. адрес заказчика
        self.organization_inn = organization_inn  # ИНН заказчика
        self.organization_kpp = organization_kpp  # КПП заказчика
        self.ogrn = ogrn  # ОГРН заказчика
        self.date_of_firm_registration = date_of_firm_registration  # Дата регистрации организации
        self.okpo = okpo  # ОКПО организации заказчика
        self.organization_rs = organization_rs  # Расчетный счет заказчика
        self.bank_name = bank_name  # Название банка заказчика
        self.bank_bik = bank_bik  # БИК банка заказчика
        self.bank_ks = bank_ks  # Корреспондентский счет банка заказчика

        self.text_6_7_deadlines_6_stages = f'''
        <h4 align="center">
        6.Сроки действия Договора
                </h4>
                <p>
                    6.1. Настоящий Договор вступает в силу с момента подписания его обеими Сторонами и действует до
                    полного
                    выполнения обязательств каждой из Сторон.
                </p>
                <p>
                    6.2. Работы по настоящему Договору начинаются с момента оплаты первого этапа работ, согласно п.3.1.
                </p>
                <h4 align="center">
                    7.Сроки выполнения работ и порядок приемки
                </h4>
                <p>
                    7.1. Разработка "Дизайн проекта" производится в течение <strong>{self.Obshiy_srok}</strong> рабочих
                    дней с
                    момента выполнения п.3.1.1., <strong>без учета времени на согласование проекта с
                    Заказчиком.</strong>
                </p>
                <p>
                    7.2. По пунктам 4.2, 4.3, 4.4. работа считается завершенной и принятой Заказчиком, а обязательства
                    Исполнителя
                    по данной работе выполненными с момента подписания акта сдачи-приемки работ.
                </p>
                <p>
                    7.3. Изменение сроков завершения работ по пунктам 4.2., 4.3., 4.4. настоящего Договора возможно в
                    случае
                    несвоевременного выполнения Заказчиком пунктов 5.1., 5.2., 5.3., 5.4., а также по взаимному
                    письменному
                    соглашению Сторон.
                </p>            
        '''  # Сроки действия Договора/ Сроки выполнения работ и порядок приемки
        self.text_4_responsibilities_of_the_contractor_full_project = f'''
                <h4 align="center">
                            4.Обязанности Исполнителя
                </h4>
                <p>
                    4.1. Исполнитель обязуется:
                </p>
                <p>
                    4.2. На основании проведенных предпроектных работ (обмеров помещения), консультаций с Заказчиком и
                    выданным
                    Заказчиком ТЗ разработать "Дизайн проект" Объекта в сроки согласованные в п.7.1., который состоит
                    из:
                </p>
                <p>
                    &nbsp;&nbsp;&nbsp;&nbsp; а) Нескольких вариантов планировки (не менее трех вариантов);
                </p>
                <p>
                    &nbsp;&nbsp;&nbsp;&nbsp; б) План обмеров
                </p>
                <p>
                    &nbsp;&nbsp;&nbsp;&nbsp; в) Предоставления рисунков перспектив для восприятия в объёме дизайнерских
                    предложений
                    (не более трех вариантов) по всем помещениям, площадь которых учтена в договорной стоимости;
                </p>
                <p>
                    &nbsp;&nbsp;&nbsp;&nbsp; г) Рисунков, где должны быть прорисованы предметы условной мебели,
                    осветительных
                    приборов, предметов декора и т.д.
                </p>
                <p>
                    &nbsp;&nbsp;&nbsp;&nbsp; е) План потолка с узлами сечений
                </p>
                <p>
                    &nbsp;&nbsp;&nbsp;&nbsp; ж) План пола
                </p>
                <p>
                    &nbsp;&nbsp;&nbsp;&nbsp; з) Кладочный план
                </p>
                <p>
                    &nbsp;&nbsp;&nbsp;&nbsp; и) План демонтажа существующих перегородок
                </p>
                <p>
                    &nbsp;&nbsp;&nbsp;&nbsp; к) Развертки по стенам
                </p>
                <p>
                    &nbsp;&nbsp;&nbsp;&nbsp; л) Схема расположения электрооборудования
                </p>
                <p>
                    &nbsp;&nbsp;&nbsp;&nbsp; м) Ведомость отделочных материалов и мебели
                </p>
                <p>
                    4.3. Информировать Заказчика, по его требованию, о ходе выполнения проектных работ.
                </p>
                <p>
                    4.4. Согласовать разработанную документацию с Заказчиком, после выполнения каждого этапа.
                </p>
                <p>
                    4.5. Исполнитель вправе от своего имени поручить выполнение отдельных работ третьим лицам только с
                    письменного
                    разрешения заказчика.
                </p>    
        '''  # Обязанности Исполнителя
        self.text_5_obligations_of_the_customer_full_project = f'''
                <h4 align="center">
        5.Обязанности Заказчика
                </h4>
                <p>
                    5.1. Предоставить Исполнителю возможность беспрепятственного натурного осмотра Объекта и выполнения
                    необходимых
                    обмеров помещения в течение одного дня с момента подписания настоящего Договора и далее по
                    необходимости.
                </p>
                <p>
                    5.2. Утвердить разработанное с помощью Исполнителя Техническое задание на разработку дизайн-проекта
                    Объекта или
                    предоставить в письменном виде замечания в течение трех дней после получения Технического задания от
                    Исполнителя.
                </p>
                <p>
                    5.3. Предоставить существующую документацию по помещению: строительные чертежи или справку БТИ, а
                    также иную
                    информацию, необходимую для составления проектной документации в течение трех дней с момента
                    подписания
                    настоящего Договора.
                </p>
                <p>
                    5.4. При возникновении у Исполнителя необходимости консультаций с Заказчиком, в ходе работ над
                    проектом,
                    провести консультацию с Исполнителем в течение одного дня с момента письменного уведомления.
                </p>
                <p>
                    5.5. В случае прекращения или приостановления работ по решению Заказчика на срок более трех месяцев,
                    произвести
                    расчет с Исполнителем согласно п.3. настоящего Договора.
                </p>
                <p>
                    5.6. Подписать акт сдачи-приемки выполненных работ или предоставить в письменном виде замечания в
                    течение пяти
                    дней после уведомления Исполнителя о выполненной работе.
                </p>
                <p>
                    5.7. Оплатить Исполнителю произведенные им работы в предусмотренном настоящим Договором порядке,
                    согласно п.3.1.
                </p>
                <p>
                    5.8. Дать согласие на размещение на сайте <a
                        href="https://www.neoluxe.ru">https://www.neoluxe.ru</a> в
                    интернете отснятого объекта вместе с сопроводительным текстом по усмотрению Исполнителя на
                    неограниченный срок с
                    полным соблюдением всей конфиденциальности, т.е. неразглашения имени заказчика, без указания адреса,
                    исходных
                    данных по метражу помещения и т. д.
                </p>
                <p>
                    5.9. Для определения стоимости работ по договору рассматривать площадь Объекта по реальным обмерам,
                    произведенным дизайнером. В случае отклонения договорной площади Объекта от площади, полученной в
                    результате
                    фактических замеров Объекта – соответственно пропорционально изменить стоимость работ.
                </p> 
        '''  # Обязанности Заказчика
        self.text_21_32_payment_procedure_full_project = f'''
        <h4 align="center">
                    2.Цена и общая сумма Договора
                </h4>
                </p>
                <p>
                    2.1. Стоимость работ по настоящему Договору составляет <strong>{self.Obshaya_summa_dogovora}
                    ({self.Obshaya_summa_dogovora_word})</strong> рублей, без НДС,
                    из расчета <strong>{self.price} ({self.M_word})</strong> рублей за один квадратный метр, без НДС
                </p>
                <p>
                    2.2. Первый этап - авансовый платеж, составляет <strong>{self.First_pay}
                    ({self.First_pay_word})</strong>
                    рублей, без НДС.
                </p>
                <p>
                    2.3. Второй этап - платеж после согласования «Планировочного решения», равен <strong>{self.Second_pay}
                    ({self.Second_pay_word})</strong> рублей, без НДС.
                </p>
                <p>
                    2.4. Третий этап - платеж после выполнения «Эскизного проекта», <strong>{self.Third_pay}
                    ({self.Third_pay_word})</strong> рублей, без НДС.
                </p>
                <p>
                    2.5. Четвертый этап - платеж после выполнения «Комплекта чертежей», <strong>{self.Fourth_pay}
                    ({self.Fourth_pay_word})</strong> рублей, без НДС.
                </p>

                <h4 align="center">
                    3.Порядок и условия оплаты
                </h4>>
                3.1. Оплата работ по настоящему Договору производится Заказчиком в течение трех банковских дней с
                момента заключения
                договора.
                </p>
                <p>
                    3.1.1. Первый этап - авансовый платеж, равный <strong>{self.First_pay}
                    ({self.First_pay_word})</strong> рублей,
                    без НДС.
                </p>
                <p>
                    3.1.2. Второй этап - платеж после согласования «Планировочного решения», составляет <strong>{self.Second_pay}
                    ({self.Second_pay_word})</strong> рублей, без НДС.
                </p>
                <p>
                    3.1.3. Третий этап - платеж после выполнения «Эскизного проекта», составляет <strong>{self.Third_pay}
                    ({self.Third_pay_word})</strong> рублей, без НДС.
                </p>
                <p>
                    3.1.4. Четвертый этап - платеж после выполнения «Комплекта чертежей», составляет <strong>{self.Fourth_pay}
                    ({self.Fourth_pay_word})</strong> рублей, без НДС.
                </p>
                <p>
                    3.2. Оплата производится безналичными платежами.
                </p>

        '''  # Цена и общая сумма Договора
        self.text_1_subject_of_the_contract_full_project = f'''
                <h4 align="center">
                    1.Предмет Договора
                </h4>
                <p>
                    1.1. Исполнитель обязуется по поручению Заказчика, в соответствии с «Техническим заданием»
                    разработать "Дизайн
                    проект" интерьера квартиры общей площадью проектирования
                    <strong>{self.square}</strong> кв. м., расположенной по адресу:
                    <strong>{self.adressofobject}</strong>,
                    именуемое в дальнейшем Объект, который включает в себя следующее:
                </p>
                <p>
                    1.1.1. "Альбом планировочных решений."
                </p>
                <p>
                    1.1.2. "Эскизный проект."
                </p>
                <p>
                    1.1.3. Предварительный подбор всех составляющих компонентов интерьера.
                </p>
                <p>
                    1.2. "Комплект чертежей."
                </p>
                <p>
                    1.3. «Техническое задание» (ТЗ) на разработку проектной документации дизайн-проекта является
                    утверждённым
                    Заказчиком документом, содержащим основную информацию об его требованиях и пожеланиях к назначению,
                    составу,
                    оборудованию, комплектации, стилистическому решению помещений объекта, а также другую информацию,
                    которая
                    является определяющей для проектирования. Согласование ТЗ происходит после подписания настоящего
                    Договора.
                </p>
                <p>
                    1.4. "Альбом планировочных решений" состоит из:
                </p>
                <p>
                    а) нескольких вариантов планировки (не менее трех вариантов);
                </p>
                <p>
                    б) план обмеров.
                </p>
                <p>
                    1.5. "Эскизный проект" это набор нескольких принципиальных решений стилистического и художественного
                    видения
                    Исполнителем будущего интерьера, в который входит:
                </p>
                <p>
                    1.5.1. Разработка общей дизайнерской концепции согласно ТЗ и условиям существующего помещения в
                    целом;
                </p>
                <p>
                    1.5.2. Исполнение перспектив будущего интерьера с использованием различных техник художественной
                    подачи
                    материала по всем помещениям, площадь которых учтена в договорной стоимости;
                </p>
                <p>
                    1.5.3. Предварительный подбор условно выбранных предметов мебели, светильников, отделочных
                    материалов и других
                    составляющих, на основе которых Исполнитель доносит до Заказчика дизайнерскую концепцию будущего
                    интерьера.
                </p>
                <p>
                    1.6. «Комплект чертежей» состоит из набора проектной документации, исполненный в виде чертежей, на
                    основе
                    которого соответствующие специалисты различного профиля могут осуществить воплощение дизайна
                    помещения,
                    разработанного Исполнителем и утверждённого Заказчиком. Комплект чертежей включает в себя:
                </p>
                <ul>
                    <li>
                        Расположение светильников, выключателей, розеток, щита, электроприборов.
                    </li>
                    <li>
                        Точки подключения сантехнических приборов.
                    </li>
                    <li>
                        Развертки стен, полов, потолков с указанием артикула применяемых материалов
                    </li>
                </ul>
                <p>
'''  # Предмет Договора
        self.text_12_bank_details_private = f'''
                <h4 align="center">
                    12.Реквизиты сторон
                </h4>

                <p>
                </p>


                <table cellpadding="1" cellspacing="1" style="width: 100%;" class="">
                    <tbody>
                    <tr>
                        <td align="left">
                            <strong>ИСПОЛНИТЕЛЬ:</strong>
                        </td>
                        <td align="left">
                            <strong>ЗАКАЗЧИК:</strong>
                        </td>
                    </tr>
                    <tr>
                        <td colspan="1" align="left">
                            ООО "Неолюкс"&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                        </td>
                        <td colspan="1" align="left">
                            {self.customername}
                        </td>
                    </tr>
                    <tr>
                        <td colspan="1" align="left">
                            350010, г. Краснодар, ул. Зиповская, д. 5&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                        </td>
                        <td colspan="1" align="left">
                            Паспорт серии: {self.passportnumber}&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                        </td>
                    </tr>
                    <tr>
                        <td colspan="1" align="left">
                            Литера Х, офис 28&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                        </td>
                        <td colspan="1" align="left">
                            Выдан: {self.issued}
                        </td>
                    </tr>
                    <tr>
                        <td colspan="1" align="left">
                            ИНН/КПП: 6658215373/231001001&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                        </td>
                        <td colspan="1" align="left">
                            {self.whenissued}
                        </td>
                    </tr>
                    <tr>
                        <td colspan="1" align="left">
                            р/с 40702810062600000113&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                        </td>
                        <td colspan="1" align="left">
                            Регистрация: {self.placeofregistration}
                        </td>
                    </tr>
                    <tr>
                        <td colspan="1" align="left">
                            ОАО «УБРиР» г. Екатеринбург&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                        </td>
                        <td colspan="1" align="left">
                            Телефон:{self.telephonenum}
                        </td>
                    </tr>
                    <tr>
                        <td colspan="1" align="left">
                            к/с 30101810900000000795&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                        </td>
                        <td colspan="1" align="left">
                            Электронная почта: {self.mail}
                        </td>
                    </tr>
                    <tr>
                        <td colspan="1" align="left">
                            БИК 046577795&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                        </td>
                    </tr>
                    </tbody>
                </table>
                <table cellpadding="1" cellspacing="1" style="width: 100%;" align="right" class="">
                    <tbody>
                    <tr>
                        <td align="left">
                            ________________________/Кандалов В.А./
                        </td>
                        <td align="right">
                            ________________________/{self.short_names()}/
                            <p>
                            </p>
                    </tr>
                    </tbody>
                    <br>
                </table>


            </div>
'''  # Реквизиты сторон физлицо
        self.text_12_bank_details_legal = f'''
                        <h4 align="center">
                            12.Реквизиты сторон
                        </h4>

                        <p>
                        </p>


                        <table cellpadding="1" cellspacing="1" style="width: 100%;" class="">
                            <tbody>
                            <tr>
                                <td align="left">
                                    <strong>ИСПОЛНИТЕЛЬ:</strong>
                                </td>
                                <td align="left">
                                    <strong>ЗАКАЗЧИК:</strong>
                                </td>
                            </tr>
                            <tr>
                                <td colspan="1" align="left">
                                    ООО "Неолюкс"&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                                </td>
                                <td colspan="1" align="left">
                                    {self.organization_name}
                                    {self.organization_inn}/{self.organization_kpp}
                                </td>
                            </tr>
                            <tr>
                                <td colspan="1" align="left">
                                    350010, г. Краснодар, ул. Зиповская, д. 5&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                                </td>
                                <td colspan="1" align="left">
                                    Адрес: {self.organization_adress}&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                                </td>
                            </tr>
                            <tr>
                                <td colspan="1" align="left">
                                    Литера Х, офис 28&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                                </td>
                                <td colspan="1" align="left">
                                    ОГРН: {self.ogrn}
                                </td>
                            </tr>
                            <tr>
                                <td colspan="1" align="left">
                                    ИНН/КПП: 6658215373/231001001&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                                </td>
                                <td colspan="1" align="left">
                                    Дата регистрации:{self.date_of_firm_registration}
                                </td>
                            </tr>
                            <tr>
                                <td colspan="1" align="left">
                                    р/с 40702810062600000113&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                                </td>
                                <td colspan="1" align="left">
                                    ОКПО: {self.okpo}
                                </td>
                            </tr>
                            <tr>
                                <td colspan="1" align="left">
                                    ОАО «УБРиР» г. Екатеринбург&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                                </td>
                                <td colspan="1" align="left">
                                    Расчетный счет: {self.organization_rs}
                                </td>
                            </tr>
                            <tr>
                                <td colspan="1" align="left">
                                    к/с 30101810900000000795&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                                </td>
                                <td colspan="1" align="left">
                                    Банк: {self.bank_name}
                                    БИК: {self.bank_bik}
                                    Корр.счет: {self.bank_ks}
                                </td>
                            </tr>
                            <tr>
                                <td colspan="1" align="left">
                                    БИК 046577795&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                                </td>
                            </tr>
                            </tbody>
                        </table>
                        <table cellpadding="1" cellspacing="1" style="width: 100%;" align="right" class="">
                            <tbody>
                            <tr>
                                <td align="left">
                                    ________________________/Кандалов В.А./
                                </td>
                                <td align="right">
                                    ________________________/{self.short_names_legal()}/
                                    <p>
                                    </p>
                            </tr>
                            </tbody>
                            <br>
                        </table>


                    </div>
        '''  # Реквизиты сторон юрлицо
        self.text = f''' 
                        {shapka_dogovora}
                        <h2 align="center">
                            ДОГОВОР № {str(self.number)}
                        </h2>
                        <table cellpadding="1" cellspacing="1" style="width: 100%;" align="right" class="">
                            <tbody>
                            <tr>
                                <td align="left">
                                    <strong>г. {self.townobject}</strong>
                                </td>
                                <td align="right">
                                    <strong>{self.date}</strong>
                                    <p>
                                    </p>
                            </tr>
                            </tbody>
                            <br>
                        </table>
                        ООО «Неолюкс», именуемое в дальнейшем «Исполнитель», в лице директора Кандалова Владимира Анатольевича,
                        действующего
                        на основании Устава предприятия, с одной стороны, и
                        <strong> {self.customername}</strong>, именуемая(ый) в дальнейшем «Заказчик», а вместе именуемые
                        «Стороны»,
                        заключили настоящий договор о нижеследующем:
                        <p>
                        </p>
                            {self.text_1_subject_of_the_contract_full_project}
                            {self.text_21_32_payment_procedure_full_project}
                            {self.text_4_responsibilities_of_the_contractor_full_project}
                            {self.text_5_obligations_of_the_customer_full_project}               
                            {self.text_6_7_deadlines_6_stages}
                            {base_text_from_8_to_11}
                            {self.text_12_bank_details_private}

        '''  # Общий Договор с физическим лицом
        self.text_legal_entity = f''' 
                                {shapka_dogovora}
                                <h2 align="center">
                                    ДОГОВОР № {str(self.number)}
                                </h2>
                                <table cellpadding="1" cellspacing="1" style="width: 100%;" align="right" class="">
                                    <tbody>
                                    <tr>
                                        <td align="left">
                                            <strong>г. {self.townobject}</strong>
                                        </td>
                                        <td align="right">
                                            <strong>{self.date}</strong>
                                            <p>
                                            </p>
                                    </tr>
                                    </tbody>
                                    <br>
                                </table>
                                ООО «Неолюкс», именуемое в дальнейшем «Исполнитель», в лице директора Кандалова Владимира Анатольевича,
                                действующего
                                на основании Устава предприятия, с одной стороны, и
                                <strong> {self.customer_firm}</strong> в лице {self.declension_of_the_word()}, действующего(ей) на основании {self.customer_legal_basis},
                                    с другой стороны, а вместе именуемые «Стороны», заключили настоящий договор о
                                нижеследующем:
                                <p>
                                </p>
                                    {self.text_1_subject_of_the_contract_full_project}
                                    {self.text_21_32_payment_procedure_full_project}
                                    {self.text_4_responsibilities_of_the_contractor_full_project}
                                    {self.text_5_obligations_of_the_customer_full_project}               
                                    {self.text_6_7_deadlines_6_stages}
                                    {base_text_from_8_to_11}
                                    {self.text_12_bank_details_legal}

                '''  # Общий Договор с юридическим лицом
        self.declension_of_the_word = self.declension_of_the_word()
        self.short_names_legal = self.short_names_legal()

    def declension_of_the_word(self):
        print("* def declension_of_the_word")
        Female_gender = False
        rp = RussianNames(count=500, patronymic=True, gender=0, surname=False, name=False, )
        rn = RussianNames(count=500, patronymic=False, gender=0, surname=False, name=True, )
        rs = RussianNames(count=500, patronymic=False, gender=0, surname=True, name=False, )

        try:
            split_name = self.customer_delegate.split()
            lastname_deligate = split_name[0]
            firstname_deligate = split_name[1]
            middlename_deligate = split_name[2]

            list = []
            list2 = []
            list3 = []
            for n in rn:
                list.append(n)
            for n in rp:
                list2.append(n)
            for n in rs:
                list3.append(n)
            if middlename_deligate in list2 or firstname_deligate in list or lastname_deligate in list3:
                Female_gender = True

            popova = morph.parse(lastname_deligate)[0]
            nelli = morph.parse(firstname_deligate)[0]
            nikolaevna = morph.parse(middlename_deligate)[0]

            if Female_gender:
                s_name = (popova.inflect({'gent', 'femn'})[0])
            else:
                s_name = (popova.inflect({'gent'})[0])
            titled_s_name = s_name.title()

            if Female_gender:
                f_name = (nelli.inflect({'gent', 'femn'})[0])
            else:
                f_name = (nelli.inflect({'gent'})[0])
            titled_f_name = f_name.title()

            if Female_gender:
                m_name = (nikolaevna.inflect({'gent', 'femn'})[0])
            else:
                m_name = (nikolaevna.inflect({'gent'})[0])
            titled_m_name = m_name.title()
            return f'{titled_s_name} {titled_f_name} {titled_m_name}'
        except:
            print("Ощибка в работе с именем заказчика")
            return 'Сергеева Аллы Светлановичем'


    # def client_id(self):
    #     with open(config.SCHETCHIK_PATH_CONTRACT3, 'rb') as f:
    #         loaded_data = pickle.load(f)  # Загружаем экземпляр класса
    #     return int(loaded_data)

    def short_names(self):
        print("* def short_names")
        full_name = self.customername
        l = full_name.split()
        new = ""
        new += l[0].title()
        r = 1
        for i in range(2):
            s = l[r]
            new += (' ' + s[0].upper() + '.')
            r += 1
        return new

    def short_names_legal(self):
        print("* def short_names_legal")
        full_name = self.customer_delegate
        l = full_name.split()
        new = ""
        new += l[0].title()
        r = 1
        for i in range(2):
            s = l[r]
            new += (' ' + s[0].upper() + '.')
            r += 1
        return new

    def to_word(self):
        print("* def to_word")
        from docxtpl import DocxTemplate
        doc = DocxTemplate(f"{self.path}dogowor_template_1.docx")
        context = {'number': self.number,
                   'townobject': self.townobject,
                   'data': self.date,
                   'customername': self.customername,
                   'square': self.square,
                   'adressofobject': self.adressofobject,
                   'Obshaya_summa_dogovora': self.Obshaya_summa_dogovora,
                   'Obshaya_summa_dogovora_word': self.Obshaya_summa_dogovora_word,
                   'First_pay': self.First_pay,
                   'First_pay_word': self.First_pay_word,
                   'Second_pay': self.Second_pay,
                   'Second_pay_word': self.Second_pay_word,
                   'Third_pay': self.Third_pay,
                   'Third_pay_word': self.Third_pay_word,
                   'Fourth_pay': self.Fourth_pay,
                   'Fourth_pay_word': self.Fourth_pay_word,
                   'Obshiy_srok': self.Obshiy_srok,
                   'passportnumber': self.passportnumber,
                   'issued': self.issued,
                   'whenissued': self.whenissued,
                   'placeofregistration': self.placeofregistration,
                   'telephonenum': self.telephonenum,
                   'mail': self.mail,
                   'short_name': self.short_names(),
                   'price_per_one_unit': self.price,
                   'M_word': self.M_word

                   }
        doc.render(context)
        doc.save(f"{config.CONTRACT_PATH}contract_{self.number}_{self.pefix}.docx")
        doc.save(f"{self.path}contract_{self.number}_{self.pefix}.docx")
        #doc.save(f"{config.CONTRACT_PATH2}contract_{self.number}_{self.pefix}.docx")

    def to_word_measurements_contract(self):
        print("* def to_word_measurements_contract")
        print(f'self.number {self.number}')
        from docxtpl import DocxTemplate
        doc = DocxTemplate(f"{config.CONTRACT_PATH}dogowor_template_measure.docx")
        context = {'number': self.number,
                   'townobject': self.townobject,
                   'data': self.date,
                   'customername': self.customername,
                   'square': self.square,
                   'adressofobject': self.adressofobject,
                   'Obshaya_summa_dogovora': self.Obshaya_summa_dogovora,
                   'Obshaya_summa_dogovora_word': self.Obshaya_summa_dogovora_word,
                   'First_pay': int(int(self.price) * int(self.square) * 0.5),
                   'First_pay_word': num2words(str(int(int(self.price) * int(self.square) * 0.5)), lang='ru'),
                   'Second_pay': int(int(self.price) * int(self.square) * 0.5),
                   'Second_pay_word': num2words(str(int(int(self.price) * int(self.square) * 0.5)), lang='ru'),
                   'Obshiy_srok': 3,
                   'passportnumber': self.passportnumber,
                   'issued': self.issued,
                   'whenissued': self.whenissued,
                   'placeofregistration': self.placeofregistration,
                   'telephonenum': self.telephonenum,
                   'mail': self.mail,
                   'short_name': self.short_names(),
                   'price_per_one_unit': self.price,
                   'M_word': self.M_word  # сумма прописью

                   }
        doc.render(context)
        doc.save(f"{config.CONTRACT_PATH}contract_{self.number}_{self.pefix}.docx")
        doc.save(f"{self.path}contract_{self.number}_{self.pefix}.docx")

    def to_word_legal(self):
        print("* def to_word_legal\n ")
        from docxtpl import DocxTemplate
        doc = DocxTemplate(f"{self.path}dogowor_template_legal.docx")
        context = {'number': self.number,
                   'townobject': self.townobject,
                   'data': self.date,
                   'customername': self.customername,
                   'square': self.square,
                   'adressofobject': self.adressofobject,
                   'Obshaya_summa_dogovora': self.Obshaya_summa_dogovora,
                   'Obshaya_summa_dogovora_word': self.Obshaya_summa_dogovora_word,
                   'First_pay': self.First_pay,
                   'First_pay_word': self.First_pay_word,
                   'Second_pay': self.Second_pay,
                   'Second_pay_word': self.Second_pay_word,
                   'Third_pay': self.Third_pay,
                   'Third_pay_word': self.Third_pay_word,
                   'Fourth_pay': self.Fourth_pay,
                   'Fourth_pay_word': self.Fourth_pay_word,
                   'Obshiy_srok': self.Obshiy_srok,
                   'passportnumber': self.passportnumber,
                   'issued': self.issued,
                   'whenissued': self.whenissued,
                   'placeofregistration': self.placeofregistration,
                   'telephonenum': self.telephonenum,
                   'mail': self.mail,
                   'short_name': self.short_names(),
                   'price_per_one_unit': self.price,
                   'M_word': self.M_word,
                   'customer_firm': self.customer_firm,
                   'declension_of_the_word': self.declension_of_the_word,
                   'customer_legal_basis': self.customer_legal_basis,
                   'organization_name': self.organization_name,
                   'organization_inn': self.organization_inn,
                   'organization_kpp': self.organization_kpp,
                   'organization_adress': self.organization_adress,
                   'ogrn': self.ogrn,
                   'date_of_firm_registration': self.date_of_firm_registration,
                   'okpo': self.okpo,
                   'organization_rs': self.organization_rs,
                   'bank_name': self.bank_name,
                   'bank_bik': self.bank_bik,
                   'bank_ks': self.bank_ks,
                   'short_names_legal': self.short_names_legal

                   }
        doc.render(context)
        try:
            file_path = f"{self.path}contract_legal_{self.number}_{self.pefix}.docx"
            print (f"{self.path}contract_legal_{self.number}_{self.pefix}.docx")
            doc.save(f"{self.path}contract_legal_{self.number}_{self.pefix}.docx")


            result = os.path.exists(file_path)
            print (f'Файл записался : {result}')
        except Exception as e:
            print(e)
