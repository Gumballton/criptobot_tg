#Работа с апи центробанка 

import requests
from my_exceptions import Cb_API_err


birja = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
ls_names = birja['Valute'].keys()

async def get_list_vals() -> list:
    try:
        lsq = []
        for i in ls_names:
            lsq.append(f"{'/'+birja['Valute'][i]['CharCode']} - {birja['Valute'][i]['Name']}")
        return lsq
    except:
        #ERRORR!!!!!
        return Cb_API_err()


async def search_val(m:str) -> str:
    birja = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
    ls_all = birja['Valute']
    try:
        if m[0] == '/':
            m = m[1:]
        if m in ['Доллар(usd)','Евро(eur)','Юань(cny)']:
            m = m.split('(')[1][:-1].upper()
        m = m.upper()
        return f"{ls_all[m]['Nominal']} {ls_all[m]['Name']} - {ls_all[m]['Value']}₽"
    except:
        #ERRORR!!!!!
        return 'Неверная валюта'
                