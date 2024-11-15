from aiogram import types, Bot, Dispatcher, executor
import configparser
from aiogram.types import Message, InputMediaPhoto, InputMediaVideo

configparser = configparser.ConfigParser()
configparser.read('config.ini')
token = configparser['telegram']['token']
admin_id = int(configparser['telegram']['admin'])

bot = Bot(token=token)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.reply("Привет, как и следует из описания это бот-предложка \nПредлагать идеи можно два раза в сутки (за спам пермач)\nНемного о боте  Весь код написала char0deyka а идея evilman'а/флейма")

@dp.message_handler(content_types=types.ContentType.ANY)
async def forward_media(message: Message):
    media_group = []
    
    if message.photo:
        media_group.append(InputMediaPhoto(media=message.photo[-1].file_id, caption=message.caption))
    elif message.video:
        media_group.append(InputMediaVideo(media=message.video.file_id, caption=message.caption))
    elif message.document:
        media_group.append(types.InputMediaDocument(media=message.document.file_id, caption=message.caption))
    elif message.voice:
        media_group.append(types.InputMediaAudio(media=message.voice.file_id, caption=message.caption))
    elif message.text:
        await bot.send_message(chat_id=admin_id, text=message.text)
    elif message.video_note:
        await bot.send_video_note(chat_id=admin_id, video_note=message.video_note.file_id)
    else:
        await message.reply(f"Неподдерживаемый тип сообщения {message.content_type}")
    if media_group:
        await bot.send_media_group(chat_id=admin_id, media=media_group)

if __name__ == '__main__':
    executor.start_polling(dp)