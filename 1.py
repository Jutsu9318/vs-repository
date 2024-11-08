from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message

bot_token = '7554379497:AAH2ZwuRWSwYqkdDDAPiiOqlDgo9HOLPwq0'
bot = Bot(token = bot_token)
dp = Dispatcher()

async def process_start_command(message: Message):
    await message.answer('hi')

async def process_help_command(message: Message):
    await message.answer('help for lossers')

async def send_photo(message: Message):
    await message.reply_photo(message.photo[0].file_id)

async def sticers(message: Message):
    await message.reply_sticker(message.sticker.file_id)

async def process_echo_command(message: Message):
    await message.reply(text = message.text)



dp.message.register(process_start_command, Command(commands='start'))
dp.message.register(process_help_command, Command(commands='help'))
dp.message.register(send_photo, F.photo)
dp.message.register(sticers, F.sticker)
dp.message.register(process_echo_command)






if __name__ == '__main__':
    dp.run_polling(bot)