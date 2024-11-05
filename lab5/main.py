import telebot
import requests
import asyncio
import random
from telebot.async_telebot import AsyncTeleBot, types
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = "7690164550:AAHdg53n9mSzlejGTD_qdbpAooYqSYcdGUg"
bot = AsyncTeleBot(TOKEN)


cathttps = [
    'https://i.pinimg.com/736x/aa/3a/3d/aa3a3dcdb73b63df7c08eb24fc4004bb.jpg',
    'https://i.pinimg.com/736x/68/c1/fa/68c1fa72de806ba5538720461084be1d.jpg',
    'https://i.pinimg.com/564x/2b/3c/4e/2b3c4ea45c1795f72ee9355476b67390.jpg',
    'https://i.pinimg.com/736x/ce/5d/64/ce5d643565a3ec9af3d900801466617b.jpg',
    'https://i.pinimg.com/736x/db/85/34/db853423f0629028407d3d565433adf2.jpg',
    'https://cdn.idaprikol.ru/images/b66f15a28c285838f280f679f119941771f87df914ca6cc279f7bee2e38f27be_1.webp',
    'https://i.pinimg.com/564x/66/59/57/665957fab77961804ce245d487dd1129.jpg',
    'https://i.pinimg.com/736x/99/9a/5e/999a5ee6841376cf56dbceed542eb7d5.jpg',
    'https://i.pinimg.com/564x/36/92/4e/36924eb74098ade895d3da4b38d7da89.jpg',
    'https://i.pinimg.com/736x/60/c9/f1/60c9f13e04d5d233334cc39fd3631977.jpg',
    'https://i.pinimg.com/736x/df/2b/6b/df2b6b24f00e51bd6f77d33ea10aa161.jpg',
    'https://i.pinimg.com/736x/e0/75/e5/e075e5f5b12f0277d6e58f772ef05530.jpg',
    'https://i.pinimg.com/564x/54/fa/2f/54fa2f339d29b9da4e6688d2d1f25b09.jpg',
    'https://i.pinimg.com/736x/fd/8d/55/fd8d5552f53925d134e6295e78fed730.jpg',
    'https://i.pinimg.com/736x/d5/17/17/d517173b450ee572d74e8e5117e81800.jpg'


]

doghttps = [
    'https://i.pinimg.com/564x/0b/8d/0a/0b8d0a0b529a3fe56ed36b28fed290bd.jpg',
    'https://i.pinimg.com/736x/47/93/a0/4793a0494a69e5672465bcc136b8940d.jpg',
    'https://i.pinimg.com/564x/7c/3b/81/7c3b81ea7380800cf006b940ae5799d5.jpg',
    'https://i.pinimg.com/564x/56/0e/ef/560eeffb2ee169455c445a1369137194.jpg',
    'https://i.pinimg.com/564x/1d/9e/13/1d9e13030d99325ad7c1cb75b56d288d.jpg',
    'https://i.pinimg.com/564x/97/f5/3f/97f53f028f6c791f6fde0d2018740c29.jpg',
    'https://i.pinimg.com/564x/6c/9d/22/6c9d220adbe62e498bc11f090aca5534.jpg',
    'https://i.pinimg.com/564x/0f/91/26/0f9126816a0810d1e1eeee8e36cff7eb.jpg',
    'https://i.pinimg.com/564x/a2/e8/7e/a2e87e5406ec546044bb5d5ae7fa79b0.jpg',
    'https://i.pinimg.com/564x/3f/83/67/3f836765f446a5188d5bb99cb49591b5.jpg',
    'https://i.pinimg.com/736x/e5/7c/96/e57c962a6589e91328daf7e723dcdc60.jpg',
    'https://i.pinimg.com/564x/70/c1/9c/70c19c086a89228f69de1be77a02085a.jpg',
    'https://i.pinimg.com/564x/43/a7/96/43a7960410385db35ab75d44010d6e01.jpg',
    'https://i.pinimg.com/736x/c7/32/c9/c732c9373f53fea994c5db5668116a76.jpg'



]

ryanhttps = [
    'https://i.pinimg.com/564x/19/dd/ac/19ddacef8e14946b73248fe5b20338b0.jpg',
    'https://i.pinimg.com/564x/35/b1/a4/35b1a465a045bc1212e11e3cdaf0b7df.jpg',
    'https://i.pinimg.com/564x/82/70/6f/82706f7dc2067284e83f7ac21aa41087.jpg',
    'https://i.pinimg.com/564x/c2/53/6f/c2536fcec9619c7ae5844f3685ccc773.jpg',
    'https://i.pinimg.com/564x/c4/ed/73/c4ed7355f28525f23e930d27c2e6cad4.jpg',
    'https://i.pinimg.com/564x/88/16/b1/8816b187e684e992d892b37317668d73.jpg',
    'https://i.pinimg.com/564x/5c/25/d5/5c25d5d0bf993bc65d59e4de97da7716.jpg',
    'https://i.pinimg.com/564x/25/4e/76/254e765ebfc7ff719d830e8f76cf27bd.jpg',
    'https://i.pinimg.com/564x/bf/5a/de/bf5ade50820ddb627e402ee0c2cbfe98.jpg',
    'https://i.pinimg.com/736x/fb/98/65/fb9865932d8f9efba79fda56981ef930.jpg',
    'https://i.pinimg.com/736x/20/62/21/2062217e83473f79e6c5b98dd10a700d.jpg',
    'https://i.pinimg.com/736x/da/ab/7b/daab7bff955698a66e3928a0d4a1144d.jpg',
    'https://i.pinimg.com/564x/b8/ab/a7/b8aba7e2ac9e78dbca075d53d26cf4c4.jpg',
    'https://i.pinimg.com/736x/b9/28/06/b92806e9c0eec93d763752b5f3f91a96.jpg',
    'https://i.pinimg.com/564x/f8/1f/8f/f81f8f8efd30ce42de13d6882d096538.jpg',
    'https://i.pinimg.com/564x/8f/d9/9f/8fd99f83d2ea84cc000306a8cc117306.jpg',
    'https://i.pinimg.com/736x/9e/0f/59/9e0f598cc43d3f662a4b3612f8c5d623.jpg',
    'https://i.pinimg.com/736x/65/ce/42/65ce42cc78a24063866d4d8f0ed314be.jpg'
]

# Функция для загрузки изображения
async def get_random_image(url):
    response = requests.get(url)
    return response.content

# Стартовое сообщение с кнопками выбора
@bot.message_handler(commands=['start'])
async def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_cat = types.KeyboardButton('Кот')
    btn_dog = types.KeyboardButton('Собака')
    btn_ryan = types.KeyboardButton('Райан Гослинг')
    markup.add(btn_cat, btn_dog, btn_ryan)

    await bot.send_message(message.chat.id, "Выбери, кого хочешь увидеть:", reply_markup=markup)

# Обработка нажатия на кнопки
@bot.message_handler(func=lambda message: True)
async def send_image(message):
    if message.text == 'Кот':
        image_url = random.choice(cathttps)
        image = await get_random_image(image_url)
        await bot.send_photo(message.chat.id, image, caption="Вот твой кот!")
    elif message.text == 'Собака':
        image_url = random.choice(doghttps)
        image = await get_random_image(image_url)
        await bot.send_photo(message.chat.id, image, caption="Вот твоя собака!")
    elif message.text == 'Райан Гослинг':
        image_url = random.choice(ryanhttps)
        image = await get_random_image(image_url)
        await bot.send_photo(message.chat.id, image, caption="Вот Райан Гослинг!")
    else:
        await bot.send_message(message.chat.id, "Я не знаю такой команды. Пожалуйста, выбери одного из предложенных!")


async def main():
    await bot.polling()

if __name__ == "__main__":
    asyncio.run(main())
