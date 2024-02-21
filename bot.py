import asyncio, django, logging, os
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.fsm_storage.redis import RedisStorage2
from tgbot.utils import set_bot_commands
from tgbot.config import load_config
from tgbot.filters.admin import AdminFilter
from tgbot.handlers.admin import register_admin
from tgbot.handlers.anketa_link import register_add_link
from tgbot.handlers.echo import register_echo
from tgbot.handlers.start import register_user
from tgbot.handlers.make_invoice import register_add_invoice
from tgbot.handlers.add_profit import register_add_profit
from tgbot.handlers.profit_counter import register_count_profit
from tgbot.handlers.add_lid import register_add_lid
from tgbot.handlers.price import register_price
from tgbot.handlers.make_contract import register_add_default_contract
from tgbot.handlers.make_measure_contract import register_add_measure_contract
from tgbot.handlers.make_legal_contract import register_add_legal_contract
from tgbot.handlers.offer import register_add_offer
from tgbot.middlewares.environment import EnvironmentMiddleware

logger = logging.getLogger(__name__)


def register_all_middlewares(dp, config):
    dp.setup_middleware(EnvironmentMiddleware(config=config))


def register_all_filters(dp):
    dp.filters_factory.bind(AdminFilter)


def register_all_handlers(dp):
    register_add_legal_contract(dp)
    register_add_offer(dp)
    register_add_default_contract(dp)
    register_add_measure_contract(dp)
    register_count_profit(dp)
    register_add_link(dp)
    register_add_profit(dp)
    register_price(dp)
    register_add_lid(dp)
    register_add_invoice(dp)
    register_admin(dp)
    register_user(dp)
    register_echo(dp)



def setup_django():
    os.environ.setdefault(
        "DJANGO_SETTINGS_MODULE",
        "dj_ac.settings"
    )
    os.environ.update({'DJANGO_ALLOW_ASYNC_UNSAFE': "true"})
    django.setup()


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
    )
    logger.info("Starting bot")
    setup_django()
    config = load_config(".env")

    storage = RedisStorage2(config.redis.host, config.redis.port, db=5, pool_size=10, prefix='bot_fsm') \
        if config.redis.use_redis else MemoryStorage()

    bot = Bot(token=config.tg_bot.token, parse_mode='HTML')
    dp = Dispatcher(bot, storage=storage)
    await set_bot_commands.set_default_commands(dp)

    bot['config'] = config

    register_all_middlewares(dp, config)
    register_all_filters(dp)
    register_all_handlers(dp)

    # start
    try:
        await dp.start_polling()

    finally:
        await dp.storage.close()
        await dp.storage.wait_closed()
        session = await bot.get_session()
        await session.close()



if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.error("Bot stopped!")
