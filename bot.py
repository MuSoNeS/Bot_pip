#!venv/bin/python
import logging
from plistlib import FMT_BINARY
from aiogram import Bot, Dispatcher, executor, types

# Объект бота
bot = Bot(token="5564701037:AAFNcZlC6UKNhmrA5D6qS1_gpVY-rDbpc8o")
# Диспетчер для бота
dp = Dispatcher(bot)
# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)


# Хэндлер на команду /test1. МОЖЕШЬ УБРАТЬ, ЕСЛИ НЕ НУЖОН
    

@dp.message_handler(content_types=[types.ContentType.ANIMATION])
async def echo_document(message: types.Message):
    await message.reply_animation(message.animation.file_id)

    #КНОПОЧКИ
    # from aiogram import types
@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Я котик!", "Комплиментик"]
    keyboard.add(*buttons)
    await message.answer("Жми быстрей на кнопку, пока не пропала!", reply_markup=keyboard)

# from aiogram.dispatcher.filters import Text
@dp.message_handler(lambda message: message.text == "Я котик!")
async def with_puree(message: types.Message):
    await message.reply("Да, ты котик!")


@dp.message_handler(lambda message: message.text == "Комплиментик")
async def without_puree(message: types.Message):
    await message.reply("Ты как всегда лучше всех!")






if __name__ == "__main__":
    # Запуск бота
    executor.start_polling(dp, skip_updates=True)