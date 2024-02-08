import pdfkit
from aiogram import Dispatcher
from aiogram import types
from aiogram.dispatcher import FSMContext

from make_contract_base.models import Organization
from tgbot.Dicts.question_list import additional_questions_for_lega_contract
from tgbot.keyboards.menu import town_menu, organisations_menu
from tgbot.misc.additional_legal_contract import Contract_legal
from tgbot.models.commands import add_contract, add_organization
from tgbot.models.contract_class import Contract

try:
    org_name = Organization.objects.get(name='ОАО Астон')
except:
    org_name = None


async def cmd_cancel(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer("Действие отменено")


async def start_making_contract(message: types.Message, state: FSMContext):
    if message.from_user.full_name == 'Vladimir Kandalov' or message.from_user.id == '1015129409':
        await message.answer("Вы начали формирование Договора на полный проект.\n"
                             "с юридическим лицом\n"
                             "Введите площадь: ")
        await state.reset_state(with_data=True)
        await state.set_state(Contract_legal.Q1)
    else:
        await state.set_state(Contract_legal.Q1)


async def validator(message: types.Message, state: FSMContext):
    if not message.text.isdigit() or len(message.text) >= 21:

        await message.reply("ведите число (не более 20 значного) ")
    else:
        await Contract_legal.next()


async def answer_q1(message: types.Message, state: FSMContext):
    await message.answer(additional_questions_for_lega_contract[1])
    answer = message.text
    async with state.proxy() as data:
        data["answer"] = answer
        print(f'answer = {answer}')

    await validator(message=message, state=Contract_legal.Q1)


async def answer_q2(message: types.Message, state: FSMContext):  # email
    await message.answer(additional_questions_for_lega_contract[2])
    answer2 = message.text
    async with state.proxy() as data:
        data["answer2"] = answer2
    await Contract_legal.next()


async def answer_q3(message: types.Message, state: FSMContext):  # Адрес объекта проектирования
    await message.answer(additional_questions_for_lega_contract[3], reply_markup=town_menu)
    answer3 = message.text
    async with state.proxy() as data:
        data["answer3"] = answer3
    await Contract_legal.next()


async def answer_q4(message: types.Message, state: FSMContext):  # Город
    await message.answer(additional_questions_for_lega_contract[4])
    answer4 = message.text
    async with state.proxy() as data:
        data["answer4"] = answer4
    await Contract_legal.next()


async def answer_q5(message: types.Message, state: FSMContext):  # Телефон заказчика:'
    await message.answer(additional_questions_for_lega_contract[5], reply_markup=organisations_menu)
    answer5 = message.text
    async with state.proxy() as data:
        data["answer5"] = answer5
    await Contract_legal.next()


async def answer_q6(message: types.Message, state: FSMContext):  # Сокращенное название организации:

    answer6 = message.text

    try:
        await message.answer("Введите полное название организации: ", reply_markup=organisations_menu)

        async with state.proxy() as data:
            data["org_name"] = message.text
        from make_contract_base.models import Organization
        organisation_name = Organization.objects.get(name=message.text)
        print(organisation_name)
        await state.set_state(Contract_legal.FIND_ADD_FIRM)
    except:
        await message.answer("0")
        await message.answer(additional_questions_for_lega_contract[6])
        async with state.proxy() as data:
            data["answer6"] = answer6
        await Contract_legal.next()


async def add_data_from_base(message: types.Message, state: FSMContext):  # Внесение данных об организации из БД:
    async with state.proxy() as data:
        orgname = data.get("org_name")

    try:
        from make_contract_base.models import Organization
        organisation_name = Organization.objects.get(name=orgname)

        async with state.proxy() as data:
            data["answer6"] = str(organisation_name.name)  # Сокращенное название организации
        async with state.proxy() as data:
            data["answer7"] = str(organisation_name.organization_full_name)  # Полное название организации:
        async with state.proxy() as data:
            data["answer8"] = str(organisation_name.organization_adress)  # Адрес организации
        async with state.proxy() as data:
            data["answer9"] = str(organisation_name.customer_delegate)  # Представитель организации заказчика
        async with state.proxy() as data:
            data["answer10"] = "Устава предприятия"  # Основание на котором действует представитель заказчика
        async with state.proxy() as data:
            data["answer11"] = str(organisation_name.organization_inn)  # ИНН
        async with state.proxy() as data:
            data["answer12"] = int(organisation_name.organization_kpp)  # КПП
        async with state.proxy() as data:
            data["answer13"] = int(organisation_name.ogrn)  # ОГРН
        async with state.proxy() as data:
            data["answer14"] = "01.01.2001"  # Дата регистрации юрлица
        async with state.proxy() as data:
            data["answer15"] = str(organisation_name.okpo)  # ОКПО
        async with state.proxy() as data:
            data["answer16"] = int(organisation_name.organization_rs)  # Р/С
        async with state.proxy() as data:
            data["answer17"] = str(organisation_name.bank_name)  # Название банка
        async with state.proxy() as data:
            data["answer18"] = str(organisation_name.bank_bik)  # БИК банка
        async with state.proxy() as data:
            data["answer19"] = int(organisation_name.bank_ks)  # К/С банка
    except Exception as e:
        await message.answer("2")
        await message.answer(str(e))
    await message.answer("цена: ")
    await state.set_state(Contract_legal.Q20)


async def answer_q7(message: types.Message, state: FSMContext):  # Сокращенное название организации:
    await message.answer(additional_questions_for_lega_contract[7])
    answer7 = message.text
    async with state.proxy() as data:
        data["answer7"] = answer7
    await Contract_legal.next()


async def answer_q8(message: types.Message, state: FSMContext):  # Юридический адрес организации заказчика
    await message.answer(additional_questions_for_lega_contract[8])
    answer8 = message.text
    async with state.proxy() as data:
        data["answer8"] = answer8
    await Contract_legal.next()


async def answer_q9(message: types.Message, state: FSMContext):  # Представитель организации заказчика
    await message.answer(additional_questions_for_lega_contract[9])
    answer9 = message.text
    listik = answer9.split(" ")
    if (len(listik)) == 3:
        async with state.proxy() as data:
            data["answer9"] = answer9
        await Contract_legal.next()
    else:
        async with state.proxy() as data:
            data["answer9"] = "Иванов Иван Иванович"
        await message.answer("Введите Фамилию Имя Отчество на русском через пробел!")
        await state.set_state(Contract_legal.Q9)


async def answer_q10(message: types.Message,
                     state: FSMContext):  # Основание на котором действует представитель заказчика
    await message.answer(additional_questions_for_lega_contract[10])
    answer10 = message.text
    async with state.proxy() as data:
        data["answer10"] = answer10

    await Contract_legal.next()


async def answer_q11(message: types.Message, state: FSMContext):  # ИНН
    await message.answer(additional_questions_for_lega_contract[11])
    answer11 = message.text
    async with state.proxy() as data:
        data["answer11"] = answer11
    await validator(message=message, state=Contract_legal.Q11)


async def answer_q12(message: types.Message, state: FSMContext):  # КПП
    await message.answer(additional_questions_for_lega_contract[12])
    answer12 = message.text
    async with state.proxy() as data:
        data["answer12"] = answer12
    await validator(message=message, state=Contract_legal.Q12)


async def answer_q13(message: types.Message, state: FSMContext):  # ОГРН
    await message.answer(additional_questions_for_lega_contract[13])
    answer13 = message.text
    async with state.proxy() as data:
        data["answer13"] = answer13
    await validator(message=message, state=Contract_legal.Q13)


async def answer_q14(message: types.Message, state: FSMContext):  # Дата регистрации юр.лица:
    await message.answer(additional_questions_for_lega_contract[14])
    answer14 = message.text
    async with state.proxy() as data:
        data["answer14"] = answer14
    await Contract_legal.next()


async def answer_q15(message: types.Message, state: FSMContext):  # ОКПО
    await message.answer(additional_questions_for_lega_contract[15])
    answer15 = message.text
    async with state.proxy() as data:
        data["answer15"] = answer15
    await validator(message=message, state=Contract_legal.Q15)


async def answer_q16(message: types.Message, state: FSMContext):  # Расчетный счет:
    await message.answer(additional_questions_for_lega_contract[16])
    answer16 = message.text
    async with state.proxy() as data:
        data["answer16"] = answer16
    await validator(message=message, state=Contract_legal.Q16)


async def answer_q17(message: types.Message, state: FSMContext):  # Название банка:
    await message.answer(additional_questions_for_lega_contract[17])
    answer17 = message.text
    async with state.proxy() as data:
        data["answer17"] = answer17
    await Contract_legal.next()


async def answer_q18(message: types.Message, state: FSMContext):  # БИК банка:
    await message.answer(additional_questions_for_lega_contract[18])
    answer18 = message.text
    async with state.proxy() as data:
        data["answer18"] = answer18
    await validator(message=message, state=Contract_legal.Q18)


async def answer_q19(message: types.Message, state: FSMContext):  # К/С банка:
    await message.answer(additional_questions_for_lega_contract[19])
    answer19 = message.text
    async with state.proxy() as data:
        data["answer19"] = answer19
    await validator(message=message, state=Contract_legal.Q19)


async def answer_q20(message: types.Message, state: FSMContext):  # цена
    async with state.proxy() as data:
        answer = data.get("answer")
        answer2 = data.get("answer2")
        answer3 = data.get("answer3")
        answer4 = data.get("answer4")
        answer5 = data.get("answer5")
        answer6 = data.get("answer6")
        answer7 = data.get("answer7")
        answer8 = data.get("answer8")
        answer9 = data.get("answer9")
        answer10 = data.get("answer10")
        answer11 = data.get("answer11")
        answer12 = data.get("answer12")
        answer13 = data.get("answer13")
        answer14 = data.get("answer14")
        answer15 = data.get("answer15")
        answer16 = data.get("answer16")
        answer17 = data.get("answer17")
        answer18 = data.get("answer18")
        answer19 = data.get("answer19")

        try:
            check = data.get("org_name")
            from make_contract_base.models import Organization
            Organization.objects.get(name=check)
        except:
            check = False
    from make_contract_base.models import ContractBase
    number_of_last_dogovor = ContractBase.objects.latest('number')
    number = (int(number_of_last_dogovor.number)) + 1
    try:
        if not check:
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print(check)

            await add_organization(
                name=answer6,
                mail=str(answer2),
                telephonenum=answer5,
                organization_full_name=answer7,
                organization_adress=answer8,
                organization_inn=answer11,
                organization_kpp=answer12,
                ogrn=answer13,
                okpo=answer15,
                organization_rs=answer16,
                bank_name=answer17,
                bank_bik=answer18,
                bank_ks=answer19)
        else:
            print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
            print(check)

        await message.answer("Запись в БД удалась")
    except Exception as e:
        await message.answer(str(e))

    try:

        new_dogovor = await Contract(
            customer_delegate=str(answer9),
            quantity=int(answer),
            prefix=2023,
            number=int(number),
            price=int(message.text),
            square=int(answer),
            mail=str(answer2),
            adressofobject=str(answer3),
            townobject=str(answer4),
            telephonenum=str(answer5),
            customer_firm=str(answer6),
            organization_full_name=answer7,
            organization_adress=answer8,
            customer_legal_basis=answer10,
            organization_inn=answer11,
            organization_kpp=answer12,
            ogrn=answer13,
            date_of_firm_registration=answer14,
            okpo=answer15,
            organization_rs=answer16,
            bank_name=answer17,
            bank_bik=answer18,
            bank_ks=answer19)

        doc = new_dogovor.text_legal_entity
        new_dogovor.path = 'C:\\Users\\User\\PycharmProjects\\tjb_2024\\tgbot\\HTML\\'
        new_dogovor.to_word_legal()
        with open(f'{new_dogovor.path}contract_legal_{new_dogovor.number}_{new_dogovor.pefix}.docx', 'rb') as g:
            await message.answer_document(g)  # Тут происходит отсылка документа пользователь.
        with open(f'{new_dogovor.path}contract_legal_{new_dogovor.number}_{new_dogovor.pefix}.html', 'w',
                  encoding='utf-8') as Html_file:
            Html_file.write(doc)
            Html_file.close()
        file = f'{new_dogovor.path}contract_legal_{new_dogovor.number}_{new_dogovor.pefix}.html'
        output = f'{new_dogovor.path}contract_legal_{new_dogovor.number}_{new_dogovor.pefix}.pdf'
        root_path = 'C:\\Users\\User\\PycharmProjects\\tjb_2024\\media\\files'
        output2 = f'{root_path}contract_legal_{new_dogovor.number}_{new_dogovor.pefix}.pdf'
        path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
        config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
        pdfkit.from_file(file, output, configuration=config)
        pdfkit.from_file(file, output2, configuration=config)  # Запись в джанго папку
        with open(output, 'rb') as pdf_file:
            await message.answer_document(pdf_file)
        await add_contract(customername=answer9,
                           quantity=int(answer),
                           price=int(message.text),
                           adressofobject=str(answer3),
                           mail=str(answer2),
                           total_cost=int(message.text) * int(answer),
                           townobject=str(answer4),
                           telephonenum=answer5,
                           customer_firm=answer6,
                           organization_full_name=answer7,
                           organization_adress=answer8,
                           customer_legal_basis=answer10,
                           organization_inn=answer11,
                           organization_kpp=answer12,
                           ogrn=answer13,
                           okpo=answer15,
                           organization_rs=answer16,
                           bank_name=answer17,
                           bank_bik=answer18,
                           bank_ks=answer19,
                           contract_file=output)
        await state.reset_state(with_data=True)
    except Exception as e:
        await message.reply("Не смог создать экземпляр класса" + str(e))
        await state.reset_state(with_data=True)


def register_add_legal_contract(dp: Dispatcher):
    dp.register_message_handler(cmd_cancel, commands=["cancel"], state="*")
    dp.register_message_handler(start_making_contract, commands=["make_legal_contract"], state="*")
    dp.register_message_handler(answer_q1, state=Contract_legal.Q1)
    dp.register_message_handler(answer_q2, state=Contract_legal.Q2)
    dp.register_message_handler(answer_q3, state=Contract_legal.Q3)
    dp.register_message_handler(add_data_from_base, state=Contract_legal.FIND_ADD_FIRM)
    dp.register_message_handler(answer_q4, state=Contract_legal.Q4)
    dp.register_message_handler(answer_q5, state=Contract_legal.Q5)
    dp.register_message_handler(answer_q6, state=Contract_legal.Q6)
    dp.register_message_handler(answer_q7, state=Contract_legal.Q7)
    dp.register_message_handler(answer_q8, state=Contract_legal.Q8)
    dp.register_message_handler(answer_q9, state=Contract_legal.Q9)
    dp.register_message_handler(answer_q10, state=Contract_legal.Q10)
    dp.register_message_handler(answer_q11, state=Contract_legal.Q11)
    dp.register_message_handler(answer_q12, state=Contract_legal.Q12)
    dp.register_message_handler(answer_q13, state=Contract_legal.Q13)
    dp.register_message_handler(answer_q14, state=Contract_legal.Q14)
    dp.register_message_handler(answer_q15, state=Contract_legal.Q15)
    dp.register_message_handler(answer_q16, state=Contract_legal.Q16)
    dp.register_message_handler(answer_q17, state=Contract_legal.Q17)
    dp.register_message_handler(answer_q18, state=Contract_legal.Q18)
    dp.register_message_handler(answer_q19, state=Contract_legal.Q19)
    dp.register_message_handler(answer_q20, state=Contract_legal.Q20)
    dp.register_message_handler(validator, state=Contract_legal.Q21)
