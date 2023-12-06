import re

import requests

def get_gas_price():
    html_text = requests.get('https://azsprice.ru/samara').text
    price = re.search(r'Аи-95 (\d\d.\d+) ₽ ', html_text).group(1)
    return float(price)


def get_power_price():
    html_text = requests.get('https://samges.ru/private/tariffs').text
    price = re.search(r'\d,\d{2}', html_text).group()
    price = price.replace(',', '.')
    return float(price)
