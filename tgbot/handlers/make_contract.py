import datetime

import pdfkit
from aiogram import Dispatcher
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove

from make_contract_base.models import PrivateContract
from tgbot.data import config
from tgbot.keyboards.menu import price_menu, town_menu
from tgbot.misc.Contract2 import Contract2
from tgbot.models.commands import add_private_contract
from tgbot.models.commands import add_private_person
from tgbot.models.contract_class import Contract
from tgbot.data import config

root_path = 'media/files'


async def to_pdf(new_dogovor, message):
    number_of_last_invoice = PrivateContract.objects.latest('id')
    dogovor_number = int(number_of_last_invoice.id) + 1
    file = f'{new_dogovor.path}contract_{dogovor_number}_{new_dogovor.pefix}.html'
    output = f'{new_dogovor.path}contract_{dogovor_number}_{new_dogovor.pefix}.pdf'
    output2 = f'{root_path}contract_{dogovor_number}_{new_dogovor.pefix}.pdf'
    path_wkhtmltopdf = 'media/wkhtmltopdf/bin/wkhtmltoimage.exe'
    config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
    pdfkit.from_file(file, output, configuration=config)
    pdfkit.from_file(file, output2, configuration=config)  # Запись в джанго папку
    with open(output, 'rb') as pdf_file:
        await message.answer_document(pdf_file)


async def cmd_reset(message: types.Message, state: FSMContext):
    photo = open('media/files/PICTURES/reset.png', 'rb')
    await message.answer_photo(photo, caption='RESET')
    await state.finish()


async def run_default_contract(message: types.Message):
    if message.from_user.full_name == 'Vladimir Kandalov' or message.from_user.id == 1015129409:
        await message.answer("Добрый день, Администратор. ID:  \n" + str(message.from_user.id) + " " +
                             "Введите Покупателя (Иванов Иван Иванович): ")
        await Contract2.first()
    else:
        await message.answer("Вы начали формирование Договора.\n"
                             "Введите Покупателя (Иванов Иван Иванович): ")
        await Contract2.first()


async def answer_q1(message: types.Message, state: FSMContext):

    number_of_last_invoice = PrivateContract.objects.latest('id')
    dogovor_number = number_of_last_invoice.id
    await message.answer("Номер текущего договора  " + str(dogovor_number))
    await message.answer("PrivateContract.objects.latest id  " + str(PrivateContract.objects.latest('id')))

    answer = message.text
    with open('media/files/customers.txt', 'a', encoding='utf-8') as f:
        f.write(str(answer)+"\n")
    with open('media/files/customers.txt', 'r', encoding='utf-8') as r:
        last_line = r.readlines()[-1]

    await message.answer(str(last_line)+" записано в текстовый файл")
    await message.reply('<a href="http://localhost:8000/media/files/customers.txt">Log_2</a>', parse_mode="HTML")
    good_fio_check = answer.split()
    if (len(good_fio_check)) == 3:
        async with state.proxy() as data:
            data["answer1"] = answer
        await message.answer("Введите <b>Площадь</b> (200): ")
        await Contract2.next()
    else:
        await message.answer("Введите ФИО полностью")
        await Contract2.first()


async def answer_q2(message: types.Message, state: FSMContext):
    answer2 = message.text  # ВВЕЛИ ПЛОЩАДЬ
    if answer2.isdigit():
        async with state.proxy() as data:
            data["answer2"] = answer2
        await message.answer("Введите <b>эл.почту</b> заказчика (ail@yandex.ru): ")
        await Contract2.next()
    else:
        await message.answer("Вы ввели не численное значение\n"
                             "Введите число:")
        await Contract2.Q2


async def answer_q3(message: types.Message, state: FSMContext):
    answer3 = message.text  # ВВЕЛИ EMAIL
    async with state.proxy() as data:
        data["answer3"] = answer3
    await message.answer("Введите <b>адрес заказчика</b> (г. Краснодар, ЖК Золотой город, ул. Городетская, д.34.) : ")
    await Contract2.next()


async def answer_q4(message: types.Message, state: FSMContext):
    answer4 = message.text  # ВВЕЛИ АДРЕС ЗАКАЗЧИКА
    async with state.proxy() as data:
        data["answer4"] = answer4
    await message.answer("Введите <b>город</b> для договора (Краснодар) : ", reply_markup=town_menu)
    await Contract2.next()


async def answer_q5(message: types.Message, state: FSMContext):
    answer5 = message.text  # ВВЕЛИ ГОРОД
    async with state.proxy() as data:
        data["answer5"] = answer5
    await message.answer("Введите серию и номер паспорта заказчика\n"
                         "(22 22 222222) : ", reply_markup=ReplyKeyboardRemove())
    await Contract2.next()


async def answer_q6(message: types.Message, state: FSMContext):
    answer6 = message.text  # ВВЕЛИ НОМЕР И СЕРИЮ ПАСПОРТА
    async with state.proxy() as data:
        data["answer6"] = answer6
    await message.answer("Введите <b>КЕМ ВЫДАН</b> паспорта заказчика\n"
                         "(Отделом УФМС России по Какой-то области в Каком-то районе г. Нска) : ")
    await Contract2.next()


async def answer_q7(message: types.Message, state: FSMContext):
    answer7 = message.text  # ВВЕЛИ КЕМ ВЫДАН ПАСПОРТ
    async with state.proxy() as data:
        data["answer7"] = answer7
    await message.answer("Введите <b>КОГДА ВЫДАН</b> паспорт заказчика\n"
                         "(2009-12-01) (Год-месяц-день) : ")
    await Contract2.next()


async def answer_q8(message: types.Message, state: FSMContext):
    answer8 = message.text  # ВВЕЛИ КОГДА ВЫДАН ПАСПОРТ
    async with state.proxy() as data:
        data["answer8"] = answer8
    await message.answer("Введите <b>АДРЕС РЕГИСТРАЦИИ</b> заказчика\n"
                         "(Республика Такая-то, г.Энск, ул. Строителей, д.1, кв.1) : ")
    await Contract2.next()


async def answer_q9(message: types.Message, state: FSMContext):
    answer9 = message.text  # ВВЕЛИ РЕГИСТРАЦИЮ ПО МЖ
    async with state.proxy() as data:
        data["answer9"] = answer9
    await message.answer("Введите <b>НОМЕР ТЕЛЕФОНА</b> заказчика\n"
                         "(+7 999 9999999) : ")
    await Contract2.next()


async def answer_q10(message: types.Message, state: FSMContext):
    answer10 = message.text  # ВВЕЛИ ТЕЛЕФОН
    async with state.proxy() as data:
        data["answer10"] = answer10
    await message.answer("Введите <b>ЦЕНУ ЗА М.КВ.</b>для заказчика\n"
                         "(1500) : ", reply_markup=price_menu)
    await Contract2.next()


async def result(message: types.Message, state: FSMContext):
    answer11 = message.text
    if answer11.isdigit():
        async with state.proxy() as data:
            data["answer11"] = answer11
            photo_d = open('media/files/PICTURES/dogovor-GPH.jpg', 'rb')
            await message.answer_photo(photo_d, caption='Готовим договор')
    else:
        await message.answer("Вы ввели не численное значение\n"
                             "Введите число:")
        await Contract2.previous()

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
        prefix = 999
    try:
        number_of_last_invoice = PrivateContract.objects.latest('id')
        dogovor_number = int(number_of_last_invoice.id) + 1
        contract_id = dogovor_number
    except:
        contract_id = 1

    new_dogovor = await Contract(customername=answer1,
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
                                 prefix=999, )
    print(f'Создан экземпляр класса договора self.number = {new_dogovor.number} !!!')
    try:
        nowd = datetime.datetime.now()
        # todo И СДЕЛАТЬ ЗАПИСЬ ЗАКАЗЧИКА СО ВСЕМИ РЕКВИЗИТАМИ В БАЗУ ДАННЫХ!
        new_contract_number = contract_id
        await add_private_contract(customername=str(answer1),
                                   quantity=int(answer2),
                                   price=int(answer2),
                                   address_of_object=answer4,
                                   town_object=answer5,
                                   private_contract_file=f'{config.CONTRACT_PATH2}contract_{new_dogovor.number}_{new_dogovor.pefix}.docx',
                                   source="Дизайн проект",
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
    doc = new_dogovor.text  # Создает договор
    new_dogovor.to_word()  # Записывает в файл ->
    #  doc.save(f"{config.CONTRACT_PATH}contract_{self.number}_{self.pefix}.docx")
    #  media/files/XLS/contract_20_999.docx

    html_file = open(f'{config.CONTRACT_PATH}contract_{contract_id}_{prefix}.html',
                     'w', encoding='utf-8')
    #  media/files/XLS/contract_20_999.html

    doc_path = (f'{config.CONTRACT_PATH}contract_{contract_id}_{prefix}.docx')
    #  media/files/XLS/contract_20_999.docx

    html_file.write(doc)  # Записывает файл
    html_file.close()
    print(f'doc_path {doc_path}')
    with open(doc_path, 'rb') as docx_file:  # Открывает и отправляет в бот
        await message.answer_document(docx_file)
    await state.reset_data()
    await state.finish()


def register_add_default_contract(dp: Dispatcher):
    dp.register_message_handler(cmd_reset, commands=["reset"], state="*")
    dp.register_message_handler(run_default_contract, commands=["make_contract"], state="*")
    dp.register_message_handler(answer_q1, state=Contract2.Q1)
    dp.register_message_handler(answer_q2, state=Contract2.Q2)
    dp.register_message_handler(answer_q3, state=Contract2.Q3)
    dp.register_message_handler(answer_q4, state=Contract2.Q4)
    dp.register_message_handler(answer_q5, state=Contract2.Q5)
    dp.register_message_handler(answer_q6, state=Contract2.Q6)
    dp.register_message_handler(answer_q7, state=Contract2.Q7)
    dp.register_message_handler(answer_q8, state=Contract2.Q8)
    dp.register_message_handler(answer_q9, state=Contract2.Q9)
    dp.register_message_handler(answer_q10, state=Contract2.Q10)
    dp.register_message_handler(result, state=Contract2.Q11)
