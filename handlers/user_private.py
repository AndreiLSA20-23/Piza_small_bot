# Сдесь все обрабоотчики событий

from aiogram import types, Router, F
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command, or_f
from aiogram.types import message
from aiogram.utils.formatting import as_list, as_marked_section, Bold #Italic, as_numbered_list и тд
from filters.chat_types import ChatTypeFilter
from kbds import reply

user_private_router = Router()
user_private_router.message.filter(ChatTypeFilter(['private']))


@user_private_router.message(CommandStart())
async def start_cmd(message: types.Message):  # Функция стартового меню
    await message.answer('Привет я виртуальный помошник', reply_markup=reply.start_kb3.as_markup(
                            resize_keyboard=True,
                            input_field_placeholder='Что Вас интересует?'))  # Стартовое сообщение меню с клавишым меню


@user_private_router.message(F.text.lower() == "меню")
@user_private_router.message(or_f(Command("menu"), (F.text.lower() == "меню")))
async def menu_cmd(message: types.Message):  # Функция вызов меню
    await message.answer(f"Вот меню") # reply_markup=reply.del_kb Удаляем или добавляем клавиатуру по необходимости


@user_private_router.message(F.text.lower() == "о магазине")
@user_private_router.message(Command("about"))
async def about_cmd(message: types.Message):
    await message.reply(f"Этот раздел  о компании Pizza&Boost")


@user_private_router.message(F.text.lower() == "варианты оплаты")
@user_private_router.message(Command("payment"))
async def payment_cmd(message: types.Message):
    text = as_list(
        as_marked_section(
            Bold("Варианты доставки/заказа:"),
            "Курьер",
            "Самовынос (сейчас прибегу заберу)",
            "Покушаю у Вас (сейчас прибегу)",
            marker='✅ '
        ),
        as_marked_section(
            Bold("Нельзя:"),
            "Почта",
            "Голуби",
            marker='❌ '
        ),
        sep='\n----------------------\n'
    )
    await message.answer(text.as_html())


@user_private_router.message((F.text.lower().contains("доставк")) | (F.text.lower() == "варианты доставки"))
@user_private_router.message(Command("shipping"))
async def shipping_cmd(message: types.Message):
    await message.answer('<b>Договор об оказании услуг и условия постаки товара.</b>')


@user_private_router.message(F.contact)
async def get_contact(message: types.Message):
    await message.answer(f"номер получен")
    await message.answer(str(message.contact))


@user_private_router.message(F.location)
async def get_location(message: types.Message):
    await message.answer(f"локация получена")
    await message.answer(str(message.location))
