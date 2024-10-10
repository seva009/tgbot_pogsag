from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import config
import subprocess

bot = Bot(token=TOKEN, disable_web_page_preview=False)
dp = Dispatcher(bot)
freq = 0
speed = 0
capcode = 0
isConfigurated = False

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Що ти лысый хочешь подорвать пейджер хезболлы? Тогда тебе сюда")

@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("/config <freq> <speed> <capcode>\nКонфиг пишется 1 раз и до рестарта бота или новой конфигурации потом что ты напишешь то и будет отправлено")

@dp.message_handler(commands=['config'])
async def process_help_command(message: types.Message):
    freq = int(message.text.split()[1])
    speed = int(message.text.split()[2])
    capcode = int(message.text.split()[3])
    isConfigurated = True

@dp.message_handler(content_types=['text'])
async def send_msg(message: types.Message):
    if not isConfigurated:
        message.reply('Ты шо лысый конфиг зделай а потом атправляй')
        return
    subprocess.run(f'echo "{capcode}:{message.text}" | sudo ./pocsag -f "{freq}" -b 0 -t 1 -r {speed}')
    message.reply("Сделано лысый")

executor.start_polling(dp) 