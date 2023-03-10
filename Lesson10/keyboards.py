from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton

kb = ReplyKeyboardMarkup(resize_keyboard=True)
b1 = KeyboardButton(text="/help")
b2 = KeyboardButton(text="/vote")

ikb = InlineKeyboardMarkup(row_width=2)
ib1 = InlineKeyboardButton(text='❤️', callback_data="like")
ib2 = InlineKeyboardButton(text='👎', callback_data="dislike")
ikb.add(ib1, ib2)
kb.add(b1,b2)