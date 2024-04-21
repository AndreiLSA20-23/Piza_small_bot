#Сдесь все обрабоотчики событий

from aiogram import types, Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import message

user_private_router = Router()


@user_private_router.message(CommandStart())
async def start_cmd(message: types.Message):  # Функция стартового меню
    await message.reply(f'Привет {message.from_user.first_name}, я виртуальный помошник')  # Стартовое сообщение

@user_private_router.message(Command('menu'))
async def menu_cmd(message: types.Message):  # Функция эхо
    # text: str | None = message.text
    #
    # if text.lower() in ['хуй', 'жопа', 'сука']:
    #     await message.answer("ВЫ Хамло")
    #
    # elif text.lower() in ['привет', 'hi']:
    #     await message.answer('Привет!!!! ')
    #
    # elif text.lower() in ['пока', ' by']:
    #     await message.answer('By')
    #
    # else:
    await message.answer(f"Вот меню")

@user_private_router.message(Command('about'))
async def about_cmd(message: types.Message):
    await message.reply(f"Этот раздел  о компании Pizza&Boost")

@user_private_router.message(Command('payment'))
async def payment_cmd(message: types.Message):
    await message.reply(f"Этот раздел оплаты от компании Pizza&Boost")

@user_private_router.message(Command('shipping'))
async def shipping_cmd(message: types.Message):
    await message.answer(f"Договор об оказании услуг и условия постаки товара")

#Пример фильтрации данных text
@user_private_router.message(F.sticker)
async def textcheack_cmd(message: types.Message):
    await message.answer(f"Вы ввели матное слово")