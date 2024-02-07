import asyncio

from tgbot.utils.db_api.postgresql import Database


async def test():
    # await db.delete_users()
    print("Создаем таблицу Пользователей...")
    await db.create_table_users()
    print("Готово")
    print("Добавляем пользователей")
    await db.add_user(7, "Second", "email", "town", "telephone", "area", "description", "source", "what_service", 3000,
                      1)

    print("Готово")
    users = await db.select_all_users()
    print(f"Получил всех пользователей: {users}")

    user = await db.select_user(nm="Second", id=7)
    print(f"Получил пользователя: {user}")


loop = asyncio.get_event_loop()
db = Database(loop)
loop.run_until_complete(test())
