#Основаная работа бота
import logging

from aiogram import executor
from aiogram import Bot, Dispatcher, types

from config import TOKEN
import markups as nav
import cbr
import bybitapi


logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

msg = ''

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
	await bot.send_message(message.from_user.id, "Добро пожаловать!\nЯ - бот отслеживания курса валют/криптовалют!", reply_markup=nav.mainq)

	
@dp.message_handler(content_types = 'text')
async def bot_message(message: types.Message):	
	if message.chat.type == 'private':
		global msg
		if message.text == '📈 КРИПТОВАЛЮТЫ':
			await bot.send_message(message.from_user.id, 'Выберите криптовалюту:', reply_markup=nav.criptoList)
			msg = message.text


		if message.text == 'ГЛАВНОЕ МЕНЮ':
			await bot.send_message(message.from_user.id, 'Выберите валюту/криптовалюту:', reply_markup=nav.mainq)
		

		if message.text == '📈 ВАЛЮТЫ':
			await bot.send_message(message.from_user.id, 'Выберите валюту', reply_markup=nav.valuelist)
			msg = message.text

		if message.text == 'Вывести список криптовалют':
			await bot.send_message(message.from_user.id, await bybitapi.get_list_cryptovals())

		if message.text == 'Вывести список валют':
			await bot.send_message(message.from_user.id, await cbr.get_list_vals())

		if message.text not in ['📈 КРИПТОВАЛЮТЫ', 'ГЛАВНОЕ МЕНЮ', '📈 ВАЛЮТЫ', 'Вывести список криптовалют', 'Вывести список валют']:
			print(message.text, msg)
			if msg == '📈 КРИПТОВАЛЮТЫ' or await cbr.search_val(message.text) == 'Неверная валюта':
				res = await bybitapi.get_cryptoval(message.text)
				if res == 'Неверная криптовалюта':
					await bot.send_message(message.from_user.id, 'Неверная криптовалюта')
				else:
					await bot.send_message(message.from_user.id, f'Криптовалюта {message.text.upper()} стоит - ${res}')
			elif msg == '📈 ВАЛЮТЫ' or await bybitapi.get_cryptoval(message.text) == 'Неверная криптовалюта':
				res = await cbr.search_val(message.text)
				print(res)
				if res == 'Неверная валюта':
					await bot.send_message(message.from_user.id, 'Неверная валюта')
				else:
					await bot.send_message(message.from_user.id, res)
		

if __name__ == '__main__':
	executor.start_polling(dp, skip_updates = True)
