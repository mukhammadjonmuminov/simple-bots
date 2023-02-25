import logging
import wikipedia
from aiogram import Bot, Dispatcher, executor, types
from environs import Env

# environs kutubxonasidan foydalanish
env = Env()
env.read_env()


API_TOKEN = env.str("API_TOKEN")
wikipedia.set_lang("uz")

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):

    await message.reply("Hi!\nI'm Wiki bot!\n"
                        "Created by: @pip_sudo ")

@dp.message_handler()
async def wiki(message: types.Message):
    try:
        respond = wikipedia.summary(message.text)
        await message.answer(respond)
    except:
        await message.answer("Bu mavzuga oid maqola topilmadi")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)