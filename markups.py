from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
btnMain = KeyboardButton("ГЛАВНОЕ МЕНЮ")
# main menu

btnSub = KeyboardButton('♥ ПОДПИСКА')
mainMenu = ReplyKeyboardMarkup(resize_keyboard = True)
mainMenu.add(btnSub)


sub_inline_markup = InlineKeyboardMarkup(row_width=1)

btnSubMonth = InlineKeyboardButton(text='Месяц - 150 рублей', callback_data='submonth')

sub_inline_markup.insert(btnSubMonth)
mainMenu = KeyboardButton('📈 ВАЛЮТЫ')
mainMenu1 = KeyboardButton('📈 КРИПТОВАЛЮТЫ')
mainq = ReplyKeyboardMarkup(resize_keyboard = True).add(mainMenu1, mainMenu)


# other menu
btnBitcoin = KeyboardButton(text='BTC', callback_data='cc_bitcoin')
btnEthereum = KeyboardButton(text='ETH', callback_data='cc_ethereum')
btnSolana = KeyboardButton(text='SOL', callback_data='cc_solana')
btnlistcripto = KeyboardButton(text='Вывести список криптовалют', callback_data='cc_ls')
criptoList = ReplyKeyboardMarkup(resize_keyboard = True).add(btnBitcoin, btnEthereum, btnSolana, btnMain, btnlistcripto)


btn_usd = KeyboardButton(text='Доллар(usd)', callback_data='cc_usd')
btn_eur = KeyboardButton(text='Евро(eur)', callback_data='cc_eur')
btn_cny = KeyboardButton(text='Юань(cny)', callback_data='cc_cny')
btnlistvalue = KeyboardButton(text='Вывести список валют', callback_data='cc_val')
valuelist = ReplyKeyboardMarkup(resize_keyboard = True).add(btn_usd, btn_eur, btn_cny, btnMain, btnlistvalue)