from aiogram import Bot, Dispatcher, executor, types
from config import TOKEN_API
from keyboards import kb, ikb
bot = Bot(TOKEN_API)
dp = Dispatcher(bot)


async def on_startup(_):
    print("I have been started up")


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id, text='Welcome to our', reply_markup=kb)


@dp.message_handler(commands=['vote'])
async def vote_command(message: types.Message):

    await bot.send_photo(chat_id=message.from_user.id, photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSHO3kLXDUcz4n10RfSO5hNrwIUxF73YauZPvYf33Ec&s",
                         caption='Как тебе?', reply_markup=ikb)

@dp.callback_query_handler()
async def vote_callback(callback: types.CallbackQuery):
        if callback.data == 'like':
            await callback.answer(text="С кайфом!")
        await callback.answer('Ну ладно(')

if __name__ == "__main__":
    executor.start_polling(dispatcher=dp, skip_updates=True, on_startup=on_startup)
