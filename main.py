import logging
from aiogram import executor
from aiogram import Bot, Dispatcher, types
import requests
from datetime import datetime
import markups as nav
from config import TOKEN

logging.basicConfig(level=logging.INFO)


bot = Bot(token=TOKEN)

dp = Dispatcher(bot)
msg = ''
birja = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
ls_names = birja['Valute'].keys()
lsq = []
for i in ls_names:
    #lsq.append([birja['Valute'][i]['CharCode'], birja['Valute'][i]['Name'], birja['Valute'][i]['Value']])
	lsq.append(f"{'/'+birja['Valute'][i]['CharCode']} - {birja['Valute'][i]['Name']}")
print(lsq)

url = 'https://api.bybit.com/v2/public/tickers'
response = requests.get(url)
data = response.json()
ls = ['/'+data['result'][i]['symbol'][:-4] for i in range(305)]
print(ls)
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
	await bot.send_message(message.from_user.id, "Добро пожаловать!\nЯ - бот отслеживания курса валют/криптовалют!", reply_markup=nav.mainq)

	
@dp.message_handler(content_types = 'text')
async def bot_message(message: types.Message):
	async def get_price(m):
				try:
					url = 'https://api.bybit.com/v2/public/tickers'
					if m[0] == '/':
						m = m[1:]
					params = {'symbol': m.upper()+'USDT'}
					response = requests.get(url, params=params)
					data = response.json()
					return float(data['result'][0]['last_price'])
				except:
					return 'Неверная криптовалюта'
				
	async def get_price_val(m):
				try:
					birja = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
					ls_names = birja['Valute']
					if m[0] == '/':
						m = m[1:]
					if m in ['Доллар(usd)','Евро(eur)','Юань(cny)']:
						m = m.split('(')[1][:-1].upper()
					return f"{ls_names[m]['Name']} стоит {ls_names[m]['Value']}"
				except:
					return 'Неверная валюта'
	
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
			await bot.send_message(message.from_user.id, ls)

		if message.text == 'Вывести список валют':
			await bot.send_message(message.from_user.id, lsq)

		if message.text not in ['📈 КРИПТОВАЛЮТЫ', 'ГЛАВНОЕ МЕНЮ', '📈 ВАЛЮТЫ', 'Вывести список криптовалют', 'Вывести список валют']:
			print(message.text, msg)
			if msg == '📈 КРИПТОВАЛЮТЫ' or await get_price_val(message.text) == 'Неверная валюта':
				res = await get_price(message.text)
				if res == 'Неверная криптовалюта':
					await bot.send_message(message.from_user.id, 'Неверная криптовалюта')
				else:
					await bot.send_message(message.from_user.id, f'Криптовалюта {message.text.upper()} стоит - ${await get_price(message.text)}')
			if msg == '📈 ВАЛЮТЫ' or await get_price(message.text) == 'Неверная криптовалюта':
				res = await get_price_val(message.text)
				if res == 'Неверная валюта':
					await bot.send_message(message.from_user.id, 'Неверная валюта')
				else:
					await bot.send_message(message.from_user.id, res)
		
	else:
		bot.send_message(message.from_user.id, 'Я тебя не понимаю(((')


if __name__ == '__main__':
	executor.start_polling(dp, skip_updates = True)
