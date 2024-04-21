# Хендлеры администрирования группой

from string import punctuation
from aiogram import F, types, Router

from matt import matt

user_group_router = Router()
restricted_words = matt


def clean_text(text: str):
    return text.translate(str.maketrans('', '', punctuation))


@user_group_router.message()
async def cleaner(message: types.Message):
    if restricted_words.intersection(clean_text(message.text.lower()).split()):
        await message.answer(f"Пользователь {message.from_user.first_name} соблюдайте правила Группы.")
        await message.delete()
        #await message.chat.ban(message.from_user_id)