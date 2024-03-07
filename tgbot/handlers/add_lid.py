from aiogram import Dispatcher
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove

from tgbot.keyboards.menu import town_menu, yes_or_no, source, services
from tgbot.misc.lids_input_states import LidsStates
from tgbot.models.commands import add_lid
from datetime import datetime

async def cmd_cancel(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer("Действие отменено")


async def input_clients_name(message: types.Message, state: FSMContext):
    await message.answer("Введите имя нового клиента: ")
    await state.set_state(LidsStates.INPUT_EMAIL)


async def input_clients_email(message: types.Message, state: FSMContext):
    clients_name = message.text
    async with state.proxy() as data:
        data["name"] = clients_name
    await message.answer("Введите email клиента: ")
    await state.set_state(LidsStates.INPUT_PHONE)


async def input_clients_phone(message: types.Message, state: FSMContext):
    email = message.text
    async with state.proxy() as data:
        data["email"] = email
    await message.answer("Введите номер телефона ")
    await state.set_state(LidsStates.INPUT_AREA)


async def input_area(message: types.Message, state: FSMContext):
    phone = message.text
    async with state.proxy() as data:
        data["phone"] = phone
    await message.answer("Введите площадь: ")
    await state.set_state(LidsStates.INPUT_DESCRIPTION)


async def input_description(message: types.Message, state: FSMContext):
    if message.text.isdigit():
        area = message.text
        async with state.proxy() as data:
            data["area"] = area
        await message.answer("Введите дополнительное описание ")
        await state.set_state(LidsStates.INPUT_SOURCE)
    else:
        await state.set_state(LidsStates.INPUT_AREA)


async def input_source(message: types.Message, state: FSMContext):
    description = message.text
    async with state.proxy() as data:
        data["description"] = description
    await message.answer("Откуда о нас узнали?", reply_markup=source)
    await state.set_state(LidsStates.INPUT_CITY)


async def input_city(message: types.Message, state: FSMContext):
    source = message.text
    async with state.proxy() as data:
        data["source"] = source
    await message.answer("Какой город?", reply_markup=town_menu)
    await state.set_state(LidsStates.INPUT_SERVICE)


async def input_service(message: types.Message, state: FSMContext):
    town = message.text
    async with state.proxy() as data:
        data["town"] = town
    await message.answer("Какая слуга нужна?", reply_markup=services)
    await state.set_state(LidsStates.INPUT_PRICE)


async def input_price(message: types.Message, state: FSMContext):
    service = message.text
    async with state.proxy() as data:
        data["service"] = service
    await message.answer("Это новый клиент? (1-да/0-нет)?", reply_markup=yes_or_no)
    await state.set_state(LidsStates.INPUT_IS_NEW)


async def input_isnew(message: types.Message, state: FSMContext):
    answerlist = [0, 1]
    if message.text.isdigit() and int(message.text) in answerlist:
        isnew = message.text
        async with state.proxy() as data:
            data["isnew"] = isnew
        await message.answer("Какая стоимость озвучена за м.кв.?", reply_markup=ReplyKeyboardRemove())
        await state.set_state(LidsStates.FINAL)
    else:
        await state.set_state(LidsStates.INPUT_IS_NEW)


async def final(message: types.Message, state: FSMContext):
    if message.text.isdigit():
        price = int(message.text)
        async with state.proxy() as data:
            data["price"] = price
            isnew = data.get("isnew")
            name = data.get("name")
            email = data.get("email")
            telephone = data.get("phone")
            area = data.get("area")
            description = data.get("description")
            source = data.get("source")
            town = data.get("town")
            what_service = data.get("service")
            our_price = price
            result = "none"
            new = 1

        try:
            # Тут записываем данные в базу данных
            frase = f"Запись {name} в файл прошла успешно"
            await message.reply(frase)

            await add_lid(new=isnew, name=name, email=email, town=town, telephone=telephone,
                          area=int(area), description=description, source=source,
                          what_service=what_service,
                          our_price=our_price, result=result)

        except Exception as e:
            await message.answer(repr(e))


    else:
        print('is not digit')
        await message.answer("Вы ввели не численное значение\n"
                             "Введите число 1 или 0:")
        await state.set_state(LidsStates.INPUT_IS_NEW)

    result_string = f'{str(datetime.now())} Имя: {name}, email: {email},Описание: {description},' \
                    f'Предложена цена: {our_price}, Услуга нужна: {what_service},Новый ли заказчик: {new},' \
                    f' Город: {town},Телефон: {telephone}, Площадь: {area}, Источник: {source}, Результат: {result}'

    with open('media/files/lids.txt', 'a', encoding='utf-8') as f:
        f.write(str(result_string) + "\n")
    with open('media/files/lids.txt', 'r', encoding='utf-8') as r:
        last_line = r.readlines()[-1]
        last_line_f = f'{last_line=}'
    await message.answer(str(last_line_f))

    await state.finish()



def register_add_lid(dp: Dispatcher):
    dp.register_message_handler(cmd_cancel, commands=["cancel"], state="*")
    dp.register_message_handler(input_clients_name, commands=["add_lid"], state="*")
    dp.register_message_handler(input_clients_email, state=LidsStates.INPUT_EMAIL)
    dp.register_message_handler(input_clients_phone, state=LidsStates.INPUT_PHONE)
    dp.register_message_handler(input_area, state=LidsStates.INPUT_AREA)
    dp.register_message_handler(input_description, state=LidsStates.INPUT_DESCRIPTION)
    dp.register_message_handler(input_source, state=LidsStates.INPUT_SOURCE)
    dp.register_message_handler(input_city, state=LidsStates.INPUT_CITY)
    dp.register_message_handler(input_service, state=LidsStates.INPUT_SERVICE)
    dp.register_message_handler(input_price, state=LidsStates.INPUT_PRICE)
    dp.register_message_handler(input_isnew, state=LidsStates.INPUT_IS_NEW)
    dp.register_message_handler(final, state=LidsStates.FINAL)
