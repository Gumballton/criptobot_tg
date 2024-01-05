#Работа с API байбита
import requests
from my_exceptions import Bybit_API_err

url = 'https://api.bybit.com/v2/public/tickers'

async def get_list_cryptovals() -> list:
    '''Получение списка доступных криптовалют'''
    try:
        response = requests.get(url)
        data = response.json()
        ls = ['/'+data['result'][i]['symbol'][:-4] for i in range(305)]

        return ls
    except:
        #ERRORR!!!!!
        return Bybit_API_err()

async def get_cryptoval(m:str) -> float | str:
    '''Получение криптовалюты по названию'''
    try:
        if m[0] == '/':
            m = m[1:]

        params = {'symbol': m.upper()+'USDT'}
        response = requests.get(url, params=params)
        data = response.json()

        return float(data['result'][0]['last_price'])
    except:
        #ERRORR
        return 'Неверная криптовалюта'