from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.utils.markdown import hcode
from tgbot.data import config
from datetime import datetime
from aiogram.utils.markdown import hlink

DATE = '%d.%m.%Y %H:%M:%S'
Log_path = config.LOG_PATH
result = "Записано в журнал" + " " + str(datetime.utcnow().strftime(DATE))

async def cmd_cancel(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer("Действие отменено")


async def bot_echo(message: types.Message):
    await message.answer(result)
    await message.reply('<a href="http://127.0.0.1:8000/media/files/logs.txt">Log</a>',parse_mode="HTML")
    textutf = (message.text)
    adding_string = str(datetime.utcnow().strftime(DATE)) + ":" + str(message.from_user.id) + ": " + textutf + "\n"
    with open(Log_path, 'a') as f:
        f.write(adding_string)




async def bot_echo_all(message: types.Message, state: FSMContext):
    state_name = await state.get_state()
    text = [
        f'Эхо в состоянии {hcode(state_name)}',
        'Содержание сообщения:',
        hcode(message.text)
    ]
    await message.answer('\n'.join(text))


def register_echo(dp: Dispatcher):
    dp.register_message_handler(cmd_cancel, commands=["cancel"], state="*")
    dp.register_message_handler(bot_echo)
    dp.register_message_handler(bot_echo_all, state="*", content_types=types.ContentTypes.ANY)
