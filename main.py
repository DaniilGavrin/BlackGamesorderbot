"""
Импортируем все необходимые модули.
aiogram - для работы и общения с ботом
asyncio - для работы с асинхронным кодом
config - для работы с конфигом, и файлом config.py (отключен для github)
"""
from aiogram import Bot, Dispatcher, types, filters
from aiogram.filters import CommandStart
from aiogram.filters.command import Command
from aiogram.types import Message
import asyncio
import config
import sqlite3

# создаем базе данных
class Database:
    def __init__(self):
        self.conn = sqlite3.connect("database.db")
        self.cursor = self.conn.cursor()
    
    def create_table(self):
        pass
        #self.cursor.execute("""CREATE TABLE IF NOT EXISTS users ( id INTEGER PRIMARY KEY, name TEXT, phone TEXT, email TEXT, password TEXT, admin INTEGER )""")

TOKEN = config.TOKEN
check_offer_done = False

dp = Dispatcher()

@dp.message(Command("price"))
async def price(message: types.Message):
    """ 
    Отвечает на команду /price
    С помощью данной команды отображаем примерный прайс наших цен.
    Разметка вывода команды Makrdown для облегченного вывода и чтения.

    """
    await message.answer(f'Цена: 1000 руб.')

@dp.message(Command("check_offer"))
async def check_offer(message: types.Message):
    """
    Обрабатываем команду /check
    В команде происходит обработка состояния заказа.
    В начале запрашиваем код заказа пользователя, и делаем запрос к базе данных, о статусе заказа.
    После получения статуса заказа отправляем сообщение с информацией о заказе.

    В случаи если данного заказа в базе нет, делаем возврат об отсутствии заказа в базе данных.
    """
    global check_offer_done
    if not check_offer_done:
        await message.answer(f'Проверка состояния заказа')
        await message.answer(f'Введите номер вашего заказа')
        check_offer_done = True

@dp.message()
async def check(message: types.Message):
    global check_offer_done
    if check_offer_done:
        await message.answer(f'Ваш заказ: {message.text}')
        await message.answer(f'Делаю запрос к базе данных')
        check_offer_done = False
        #запрашиваем user_id пользователя
        user_id = message.from_user.id
        await message.answer(f'Ваш id: {user_id}')
                                
    else:
        await message.answer(f'Некорректный запрос!')
                
                

    

@dp.message(Command("create_offer"))
async def create_offer(message: types.Message):
    """
    Команда для создания заказа.
    При запуске команды запускаем стартовое сообщение, и показываем пользователю то что он может выбрать.
    Ожидаем выбор пользователя и записываем результат в переменную.
    И так со всеми шагами, в кажддом шаге выводим предварительную стоимость.
    Спрашиваем у пользователя кто он? Юридическое или физическое лицо.
    Если пользователь ответил Юридическое лицо, то запрашиваем название компании и ИНН
    Если ответил физическое лицо, то запрашиваем его имя и фамилию, а также номер телефона в формате +7-(xxx)-xxx-xx-xx
    После получения данных о заказчике создаем через генератор счет с информацией об услугах.
    Также ниже формируем qr-код на оплату услуг.
    """
    await message.answer(f'Создаю запрос на заказ...')

@dp.message(CommandStart())
async def start(message: types.Message):
    """
    обработчик команды /start
    Выводим пользователю стартовое ознокомительное сообщение по нашему боту.
    Разметка вывода = Markdown
    """
    await message.answer(f"Привет, {message.from_user.full_name}! \nЯ, бот для управления заказами. \n\nВведите команду /help для получения дополнительной информации.")

async def main() -> None:
    bot = Bot(TOKEN)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())