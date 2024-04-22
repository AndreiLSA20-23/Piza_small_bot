#Расположение кнопок в стартовом меню([[]]-один ряд, [[],{}]- два ряда
from aiogram.types import KeyboardButtonPollType, ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.utils.keyboard import ReplyKeyboardBuilder

#Двухрядная клавиатура
start_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Меню"),
            KeyboardButton(text="О магазине"),
        ],
        {
            KeyboardButton(text="Варианты доставки"),
            KeyboardButton(text="Варианты оплаты"),
        }
    ],
    resize_keyboard=True,
    input_field_placeholder='Что Вас интересует?'
)
#Удаляем клавивтуру при нажатии на меню второй раз
del_kbd = ReplyKeyboardRemove()


start_kb2 = ReplyKeyboardBuilder()
start_kb2.add(
    KeyboardButton(text="Меню"),
    KeyboardButton(text="О магазине"),
    KeyboardButton(text="Варианты доставки"),
    KeyboardButton(text="Варианты оплаты"),
)
start_kb2.adjust(3,1)


start_kb3 = ReplyKeyboardBuilder()
start_kb3.attach(start_kb2)
start_kb3.row(KeyboardButton(text="Оставить отзыв"),)


test_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Создать опрос", request_poll=KeyboardButtonPollType()),
        ],
        [
            KeyboardButton(text="Отправить номер ☎️", request_contact=True),
            KeyboardButton(text="Отправить локацию 🗺️", request_location=True),
        ],
    ],
    resize_keyboard=True,
)
