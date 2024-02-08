import datetime
import pdfkit
from aiogram import Dispatcher
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove

from tgbot.data import config
from make_contract_base.models import PrivateContract
from tgbot.keyboards.menu import town_menu
from tgbot.misc.measure_contract import Measure
from tgbot.models.contract_class import Contract
from tgbot.models.commands import add_private_contract
from tgbot.models.commands import add_private_person

try:
    number_of_last_invoice = PrivateContract.objects.latest('id')
except:
    number_of_last_invoice = 0




root_path = 'C:\\Users\\User\\PycharmProjects\\tjb_2024\\media\\files'


async def to_pdf(new_dogovor, message):

    file = f'{new_dogovor.path}contract_{new_dogovor.number}_{new_dogovor.pefix}.html'
    output = f'{new_dogovor.path}contract_{new_dogovor.number}_{new_dogovor.pefix}.pdf'
    root_path = 'C:\\Users\\User\\PycharmProjects\\tjb_2024\\media\\files'
    output2 = f'{root_path}contract_{new_dogovor.number}_{new_dogovor.pefix}.pdf'
    path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
    configuration = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
    pdfkit.from_file(file, output, configuration=configuration)
    pdfkit.from_file(file, output2, configuration=configuration)  # Запись в джанго папку
    with open(output, 'rb') as pdf_file:
        await message.answer_document(pdf_file)


async def run_measure_contract(message: types.Message):
    if message.from_user.full_name == 'Vladimir Kandalov' or message.from_user.full_name == 'Olga Zavada':
        await message.answer("Вы начали формирование Договора (Обмеры).\n"
                             "Введите Покупателя (Иванов Иван Иванович): ")
        await Measure.first()
    else:
        await Measure.first()


async def answer_q1(message: types.Message, state: FSMContext):
    answer = message.text
    good_fio_check = answer.split()
    if (len(good_fio_check)) == 3:
        async with state.proxy() as data:
            data["answer1"] = answer
        await message.answer("Введите <b>Площадь</b> (200): ")
        await Measure.next()
    else:
        await message.answer("Введите ФИО полностью")
        await Measure.first()


async def answer_q2(message: types.Message, state: FSMContext):
    answer2 = message.text  # ВВЕЛИ ПЛОЩАДЬ
    if answer2.isdigit():
        async with state.proxy() as data:
            data["answer2"] = answer2
        await message.answer("Введите <b>эл.почту</b> заказчика (ail@yandex.ru): ")
        await Measure.next()
    else:
        await message.answer("Вы ввели не численное значение\n"
                             "Введите число:")
        await Measure.Q2


async def answer_q3(message: types.Message, state: FSMContext):
    answer3 = message.text  # ВВЕЛИ EMAIL
    async with state.proxy() as data:
        data["answer3"] = answer3
    await message.answer("Введите <b>адрес заказчика</b> (г. Краснодар, ЖК Золотой город, ул. Городетская, д.34.) : ")
    await Measure.next()


async def answer_q4(message: types.Message, state: FSMContext):
    answer4 = message.text  # ВВЕЛИ АДРЕС ЗАКАЗЧИКА
    async with state.proxy() as data:
        data["answer4"] = answer4
    await message.answer("Введите <b>город</b> для договора (Краснодар) : ", reply_markup=town_menu)
    await Measure.next()


async def answer_q5(message: types.Message, state: FSMContext):
    answer5 = message.text  # ВВЕЛИ ГОРОД
    async with state.proxy() as data:
        data["answer5"] = answer5
    await message.answer("Введите серию и номер паспорта заказчика\n"
                         "(22 22 222222) : ", reply_markup=ReplyKeyboardRemove())
    await Measure.next()


async def answer_q6(message: types.Message, state: FSMContext):
    answer6 = message.text  # ВВЕЛИ НОМЕР И СЕРИЮ ПАСПОРТА
    async with state.proxy() as data:
        data["answer6"] = answer6
    await message.answer("Введите <b>КЕМ ВЫДАН</b> паспорта заказчика\n"
                         "(Отделом УФМС России по Какой-то области в Каком-то районе г. Нска) : ")
    await Measure.next()


async def answer_q7(message: types.Message, state: FSMContext):
    answer7 = message.text  # ВВЕЛИ КЕМ ВЫДАН ПАСПОРТ
    async with state.proxy() as data:
        data["answer7"] = answer7
    await message.answer("Введите <b>КОГДА ВЫДАН</b> паспорт заказчика\n"
                         "(2009-11-23) Год-месяц-день : ")
    await Measure.next()


async def answer_q8(message: types.Message, state: FSMContext):
    answer8 = message.text  # ВВЕЛИ КОГДА ВЫДАН ПАСПОРТ
    async with state.proxy() as data:
        data["answer8"] = answer8
    await message.answer("Введите <b>АДРЕС РЕГИСТРАЦИИ</b> заказчика\n"
                         "(Республика Такая-то, г.Энск, ул. Строителей, д.1, кв.1) : ")
    await Measure.next()


async def answer_q9(message: types.Message, state: FSMContext):
    answer9 = message.text  # ВВЕЛИ РЕГИСТРАЦИЮ ПО МЖ
    async with state.proxy() as data:
        data["answer9"] = answer9
    await message.answer("Введите <b>НОМЕР ТЕЛЕФОНА</b> заказчика\n"
                         "(+7 999 9999999) : ")
    await Measure.next()


async def answer_q10(message: types.Message, state: FSMContext):
    answer10 = message.text  # ВВЕЛИ ТЕЛЕФОН
    async with state.proxy() as data:
        data["answer10"] = answer10
    await message.answer("Введите <b>ЦЕНУ ЗА М.КВ.</b>для заказчика\n"
                         "(1500) : ")
    await Measure.next()


async def result(message: types.Message, state: FSMContext):
    answer11 = message.text
    await message.answer(f'Вы ввели:{message.text}')
    if answer11.isdigit():
        async with state.proxy() as data:
            data["answer11"] = answer11
            await message.answer('Готовим договор.')
    else:
        await message.answer("Вы ввели не численное значение\n"
                             "Введите число:")
        await Measure.previous()

    async with state.proxy() as data:
        answer1 = data.get("answer1")
        answer2 = data.get("answer2")
        answer3 = data.get("answer3")
        answer4 = data.get("answer4")
        answer5 = data.get("answer5")
        answer6 = data.get("answer6")
        answer7 = data.get("answer7")
        answer8 = data.get("answer8")
        answer9 = data.get("answer9")  # Регистрация...
        answer10 = data.get("answer10")  # +7978 076088
        answer11 = data.get("answer11")  # 1500
        prefix = 888

    try:
        contract_id = int(number_of_last_invoice.id) + 1
    except:
        contract_id = 1
    print (f'number_of_last_invoice==contract_id {number_of_last_invoice==contract_id}')
    new_m_dogovor = await Contract(customername=answer1,
                                   quantity=int(answer2),
                                   price=int(answer11),
                                   square=int(answer2),
                                   mail=answer3,
                                   number=contract_id,
                                   adressofobject=answer4,
                                   townobject=answer5,
                                   passportnumber=answer6,
                                   issued=answer7,
                                   whenissued=answer8,
                                   placeofregistration=answer9,
                                   telephonenum=answer10,
                                   prefix=888,
                                   )
    print(f'Создан экземпляр класса договора self.number = {new_m_dogovor.number} !!!')
    new_m_dogovor.to_word_measurements_contract()
    text = (f'new_m_dogovor.number {new_m_dogovor.number}')
    await message.answer(text)
    try:
        nowd = datetime.datetime.now()
        # todo И СДЕЛАТЬ ЗАПИСЬ ЗАКАЗЧИКА СО ВСЕМИ РЕКВИЗИТАМИ В БАЗУ ДАННЫХ!
        new_contract_number = (int(number_of_last_invoice.id)) + 1
        await add_private_contract(customername=str(answer1),
                                   quantity=int(answer2),
                                   price=int(answer2),
                                   address_of_object=answer4,
                                   town_object=answer5,
                                   private_contract_file=f'{config.CONTRACT_PATH2}contract_{new_contract_number}_{new_m_dogovor.pefix}.docx',
                                   source="Обмеры",
                                   square=int(answer2),
                                   published=f'{nowd.year}-{nowd.month}-{nowd.day}'
                                   )
    except Exception as e:
        print(f'customername= {answer1}')
        print(e)

    try:
        await add_private_person(customername=str(answer1),
                                 mail=str(answer3),
                                 passportnumber=str(answer6),
                                 issued=str(answer7),
                                 whenissued=answer8,
                                 placeofregistration=str(answer9),
                                 telephonenum=answer10,
                                 )
        await message.answer("Успешно сделана запись заказчика в б.д.")
    except Exception as e:
        await message.answer(str(e))
        await message.answer("Не получается записать покупателя в базу данных")
    with open(
            f'{config.CONTRACT_PATH}contract_{new_m_dogovor.number}_{prefix}.docx',
            'rb') as g:
        await message.answer_document(g)
        await message.answer('Запись удалась')
    # doc_path = (f'{config.CONTRACT_PATH}contract_{new_m_dogovor.number}_{prefix}.docx')
    # with open(doc_path, 'rb') as docx_file:
    #     await message.answer_document(docx_file)

    await state.reset_state(with_data=True)


def register_add_measure_contract(dp: Dispatcher):
    dp.register_message_handler(run_measure_contract, commands=["make_measuring_contract"], state="*")
    dp.register_message_handler(answer_q1, state=Measure.Q1)
    dp.register_message_handler(answer_q2, state=Measure.Q2)
    dp.register_message_handler(answer_q3, state=Measure.Q3)
    dp.register_message_handler(answer_q4, state=Measure.Q4)
    dp.register_message_handler(answer_q5, state=Measure.Q5)
    dp.register_message_handler(answer_q6, state=Measure.Q6)
    dp.register_message_handler(answer_q7, state=Measure.Q7)
    dp.register_message_handler(answer_q8, state=Measure.Q8)
    dp.register_message_handler(answer_q9, state=Measure.Q9)
    dp.register_message_handler(answer_q10, state=Measure.Q10)
    dp.register_message_handler(result, state=Measure.Q11)
