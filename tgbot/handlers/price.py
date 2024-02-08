from aiogram import Dispatcher
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove

from Classes.CalcClasses import ProjectPrice
from constants.models import Constants
from tgbot.keyboards.uslugi import *
from tgbot.misc.price_list import PriceList


async def cmd_cancel(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer("Действие отменено")

async def price_start(message: types.Message, state: FSMContext):
    if message.from_user.full_name == 'Vladimir Kandalov' or message.from_user.full_name == 'Olga Zavada':
        await message.answer('Введите площадь (200):')
        await state.set_state(PriceList.Q1)
    else:
        await message.answer("У Вас нет разрешения")
       # await state.reset_state(with_data=True)
    await message.answer('Введите площадь (200):')
    await state.set_state(PriceList.Q1)


async def answer_q1(message: types.Message, state: FSMContext):
    answer = message.text
    if answer.isdigit():
        async with state.proxy() as data:
            data["answer"] = answer
        await message.answer('Введите количество комнат:')
        await state.set_state(PriceList.Q2)
    else:
        await message.answer('Введите числовое значение!')
        await PriceList.previous()


async def answer_q2(message: types.Message, state: FSMContext):
    answer2 = message.text
    if answer2.isdigit():
        async with state.proxy() as data:
            data["answer2"] = answer2
        await message.answer('Укажите состав проекта:', reply_markup=uslugi)
        await PriceList.next()
    else:
        await message.answer('Введите числовое значение!', reply_markup=ReplyKeyboardRemove())
        await PriceList.previous()


async def answer_q3(message: types.Message, state: FSMContext):
    answer3 = message.text
    if ',' in answer3:

        answer3 = answer3.split(',')
        async with state.proxy() as data:
            data["answer3"] = answer3

        await message.answer('Кол-во дизайнеров:', reply_markup=ReplyKeyboardRemove())
        await PriceList.next()

    elif answer3 == 'Обмеры (70)':
        answer7 = ['обмеры']
        async with state.proxy() as data:
            data["answer3"] = answer7
        await message.answer('Кол-во дизайнеров:', reply_markup=ReplyKeyboardRemove())
        await PriceList.next()
    elif answer3 == 'Планировочные решения (150)':
        answer7 = ['альбом планировочных решений']
        async with state.proxy() as data:
            data["answer3"] = answer7
        await message.answer('Кол-во дизайнеров:', reply_markup=ReplyKeyboardRemove())
        await PriceList.next()
    elif answer3 == 'Фор-проект (400)':
        answer7 = ['фор-проект']
        async with state.proxy() as data:
            data["answer3"] = answer7
        await message.answer('Кол-во дизайнеров:', reply_markup=ReplyKeyboardRemove())
        await PriceList.next()
    elif answer3 == 'Д.П.с комплектацией':
        answer7 = ['обмеры', 'электрика', 'планировка', 'кладочный план', 'демонтаж', 'план ТП', 'развертки',
                   'ведомость',
                   'план пола', 'план потолка', 'мебельные конструкции', 'визуализация', 'обложка',
                   'электрика освещение',
                   'электрика розетки', 'узлы потолка', 'примечание', 'ведомость электроустановки', 'ведомость дверей',
                   'схема разверток стен', 'cхема сан.тех.приборов', 'комплектация']
        async with state.proxy() as data:
            data["answer3"] = answer7
        await message.answer('Кол-во дизайнеров:', reply_markup=ReplyKeyboardRemove())
        await PriceList.next()

    elif answer3 == 'Полный дизайн проект (1500)':
        answer7 = ['обмеры', 'электрика', 'планировка', 'кладочный план', 'демонтаж', 'план ТП', 'развертки',
                   'ведомость',
                   'план пола', 'план потолка', 'мебельные конструкции', 'визуализация', 'обложка',
                   'электрика освещение',
                   'электрика розетки', 'узлы потолка', 'примечание', 'ведомость электроустановки', 'ведомость дверей',
                   'схема разверток стен', 'cхема сан.тех.приборов']
        async with state.proxy() as data:
            data["answer3"] = answer7
        await message.answer('Кол-во дизайнеров:', reply_markup=ReplyKeyboardRemove())
        await PriceList.next()

    elif answer3 == 'Д.П.с комплектацией и авторским (2200)':
        answer7 = ['обмеры', 'электрика', 'планировка', 'кладочный план', 'демонтаж', 'план ТП', 'развертки',
                   'ведомость',
                   'план пола', 'план потолка', 'мебельные конструкции', 'визуализация', 'обложка',
                   'электрика освещение',
                   'электрика розетки', 'узлы потолка', 'примечание', 'ведомость электроустановки', 'ведомость дверей',
                   'схема разверток стен', 'cхема сан.тех.приборов', 'комплектация', 'авторский надзор']
        async with state.proxy() as data:
            data["answer3"] = answer7
        await message.answer('Кол-во дизайнеров:', reply_markup=ReplyKeyboardRemove())
        await PriceList.next()

    elif answer3 == 'Д.П.с авторским (1800)':
        answer7 = ['обмеры', 'электрика', 'планировка', 'кладочный план', 'демонтаж', 'план ТП', 'развертки',
                   'ведомость',
                   'план пола', 'план потолка', 'мебельные конструкции', 'визуализация', 'обложка',
                   'электрика освещение',
                   'электрика розетки', 'узлы потолка', 'примечание', 'ведомость электроустановки', 'ведомость дверей',
                   'схема разверток стен', 'cхема сан.тех.приборов', 'авторский надзор']
        async with state.proxy() as data:
            data["answer3"] = answer7
        await message.answer('Кол-во дизайнеров:', reply_markup=ReplyKeyboardRemove())
        await PriceList.next()

    else:
        async with state.proxy() as data:
            data["answer3"] = answer3
        await message.answer('Кол-во дизайнеров:')
        await PriceList.next()


async def answer_q4(message: types.Message, state: FSMContext):
    answer4 = message.text
    if answer4.isdigit():
        async with state.proxy() as data:
            data["answer4"] = answer4
        await message.answer('Кол-во чертёжников:')
        await PriceList.next()
    else:
        await message.answer('Введите числовое значение!')
        await PriceList.previous()


async def answer_q5(message: types.Message, state: FSMContext):

    wageOfDraftsmen = int(Constants.objects.get(key='wageOfDraftsmen').value)
    wageOfDesigner = int(Constants.objects.get(key='wageOfDesigner').value)
    from_db = Constants.objects.get(key='profit_norm_perm_max')
    profit_norm_perm_max = int(from_db.value)
    profit_norm_perm_min = int(Constants.objects.get(key='profit_norm_perm_min').value)
    nov = int(Constants.objects.get(key='timeOfVis').value)

    answer5 = message.text
    if answer5.isdigit():
        async with state.proxy() as data:
            data["answer5"] = answer5
        async with state.proxy() as data:
            answer = data.get("answer")
            answer2 = data.get("answer2")
            answer3 = data.get("answer3")
            answer4 = data.get("answer4")

        newInterior_min = ProjectPrice(square=int(answer), spaces=int(answer2), typeof=1, content=answer3,
                                       designers=int(answer4),
                                       draftsmen=int(answer5), profit_norm_perm=profit_norm_perm_min,
                                       wage_of_designer=wageOfDesigner,
                                       wage_of_draftsmen=wageOfDraftsmen, time_of_one_vis=nov)

        """wageOfDesigner = 400  # Гонорар дизайнера за квадрат
        self.wageOfDraftsmen"""

        newInterior_max = ProjectPrice(square=int(answer), spaces=int(answer2), typeof=1, content=answer3,
                                       designers=int(answer4),
                                       draftsmen=int(answer5), profit_norm_perm=profit_norm_perm_max,
                                       wage_of_designer=wageOfDesigner,
                                       wage_of_draftsmen=wageOfDraftsmen, time_of_one_vis=nov)

        t = newInterior_min.time_of_visualization(newInterior_min.spaces, newInterior_min.designers)
        r = newInterior_min.time_of_blueprints(newInterior_min.spaces, newInterior_min.draftsmen)
        o = newInterior_min.overhead(newInterior_min.square, newInterior_min.time_of_visualization(newInterior_min.spaces,
                                                                                                   newInterior_min.designers),
                                     newInterior_min.time_of_blueprints(newInterior_min.spaces,
                                                                        newInterior_min.draftsmen))
        p = newInterior_min.project_parts()

        o1 = newInterior_max.overhead(newInterior_max.square,
                                      newInterior_min.time_of_visualization(newInterior_max.spaces,
                                                                            newInterior_max.designers),
                                      newInterior_max.time_of_blueprints(newInterior_max.spaces,
                                                                         newInterior_max.draftsmen))
        try:
            await message.answer(
                f'<b>Время на визуализацию</b>: {t}\n<b>Время на чертежи:</b> {r}\n<b>Общее время:</b> {t + r}\n<b>Цена за м.кв.минимальная:</b> {o}\n'
                f'<b>Цена за м.кв. максимальная:</b> {o1}\n<b>Часть проекта:</b> {p}\n'
                f'<b>Состав проекта:</b> {newInterior_min.content}')
            await state.reset_state(with_data=True)
        except Exception as e:
            await message.answer(str(e))
            await state.reset_state(with_data=True)

    else:
        await message.answer('Введите числовое значение!')
        await PriceList.previous()
#todo сделать расчет параллельной работы

def register_price(dp: Dispatcher):
    dp.register_message_handler(cmd_cancel, commands=["cancel"], state="*")
    dp.register_message_handler(price_start, commands=["price"], state="*")
    dp.register_message_handler(answer_q1, state=PriceList.Q1)
    dp.register_message_handler(answer_q2, state=PriceList.Q2)
    dp.register_message_handler(answer_q3, state=PriceList.Q3)
    dp.register_message_handler(answer_q4, state=PriceList.Q4)
    dp.register_message_handler(answer_q5, state=PriceList.Q5)
