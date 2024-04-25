# Хендлеры администрирования группой
from string import punctuation, digits

from aiogram import F, Bot, types, Router
from aiogram.filters import Command

from filters.chat_types import ChatTypeFilter
from common.restricted_words import restricted_words


user_group_router = Router()
user_group_router.message.filter(ChatTypeFilter(["group", "supergroup"]))
user_group_router.edited_message.filter(ChatTypeFilter(["group", "supergroup"]))


@user_group_router.message(Command("admin"))
async def get_admins(message: types.Message, bot: Bot):
    chat_id = message.chat.id
    admins_list = await bot.get_chat_administrators(chat_id)
    #просмотреть все данные и свойства полученных объектов
    #print(admins_list)
    # Код ниже это генератор списка, как и этот x = [i for i in range(10)]
    admins_list = [
        member.user.id
        for member in admins_list
        if member.status == "creator" or member.status == "administrator"
    ]
    bot.my_admins_list = admins_list
    if message.from_user.id in admins_list:
        await message.delete()
    #print(admins_list)


def clean_text(text: str):
    pun = digits + punctuation
    return text.translate(str.maketrans("", "", pun))


@user_group_router.edited_message()
@user_group_router.message()
async def cleaner(message: types.Message):
    msn = clean_text(message.text.lower())
    if restricted_words.intersection(msn.split()):
        await message.answer(
            f"{message.from_user.first_name}, соблюддайте порядок в чате!"
        )
        await message.delete()
        # await message.chat.ban(message.from_user.id)