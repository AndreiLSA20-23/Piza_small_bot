import os
import asyncio

from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.fsm.strategy import FSMStrategy
from aiogram.types import BotCommandScopeAllPrivateChats
from dotenv import find_dotenv, load_dotenv
from aiogram.client.bot import DefaultBotProperties

from handlers.admin_private import admin_router

load_dotenv(find_dotenv())  # Работа с ключем токеном

from handlers.user_private import user_private_router
from handlers.user_group import user_group_router
from common.bot_cmds_list import private

bot = Bot(token=os.getenv('TOKEN'), default=DefaultBotProperties(parse_mode=ParseMode.HTML))  # Экземпляр класса бот
bot.my_admins_list = []



dp = Dispatcher(fsm_strategy=FSMStrategy.USER_IN_CHAT)  # Экземпляр класса отвечающий за сообщения от сервера телеграмм.
ALLOWED_UPDATES = ['message', 'edited_message']

dp.include_router(user_private_router)
dp.include_router(user_group_router)
dp.include_router(admin_router)

async def main():
    await bot.delete_webhook(drop_pending_updates=True)  # Отлюкаем обработку событий при выключеном боте
    #await bot.delete_my_commands(scope=types.BotCommandScopeAllPrivateChats())
    await bot.set_my_commands(commands=private, scope=types.BotCommandScopeAllPrivateChats())
    await dp.start_polling(bot, allowed_updates=ALLOWED_UPDATES)


asyncio.run(main())
