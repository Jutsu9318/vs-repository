from aiogram import Bot, Dispatcher
from aiogram.types import Message
BT = '7554379497:AAH2ZwuRWSwYqkdDDAPiiOqlDgo9HOLPwq0'
bot = Bot(token = BT)
dp = Dispatcher()
def my_start_filter(message: Message) -> bool:
    return message.text == '/start'
@dp.message(my_start_filter)
async def my_start(message: Message):
    print(message.model_dump_json(indent=4, exclude_none=True))
    await message.answer(text = 'this is start command')

if __name__ == '__main__':
    dp.run_polling(bot)