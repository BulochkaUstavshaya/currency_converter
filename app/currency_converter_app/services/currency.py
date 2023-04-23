import requests
import xmltodict
from dataclasses import dataclass


@dataclass
class Currency:
    char_code: str
    nominal_cost: int
    value_in_rub: float


def convert_currencies(currency_from: str, currency_into: str, value: float) -> float:
    '''
    Transfers currencies with the help of a Russian bank
    '''
    v1, v2 = 0, 0
    exchange_rates = get_exchange_rates()
    for item in exchange_rates:
        if item.char_code == currency_into:
            v1 = item
        elif item.char_code == currency_from:
            v2 = item

    if not v1 and not v2:
        return value
    if not v1:
        return value * v2.value_in_rub / v2.nominal_cost
    if not v2:
        return value / v1.value_in_rub * v1.nominal_cost
    return value * v1.value_in_rub / v1.nominal_cost * v2.value_in_rub / v2.value_in_rub


def get_exchange_rates() -> list[Currency]:
    '''
    Receives the exchange rates of all currencies against the RUB
    '''
    response = requests.get('https://www.cbr.ru/scripts/XML_daily.asp?')
    exchange_rates = xmltodict.parse(response.text)['ValCurs']['Valute']
    result = []
    for item in exchange_rates:
        to_float = item['Value'].split(',')
        result.append(Currency(item['CharCode'], int(item['Nominal']), float(f'{to_float[0]}.{to_float[1]}')))
    return result


def get_currency_names() -> list:
    response = requests.get('https://www.cbr.ru/scripts/XML_daily.asp?')
    currencies = xmltodict.parse(response.text)
    result = [('RUB', 'RUB'), ]
    for item in currencies['ValCurs']['Valute']:
        result.append((item['CharCode'], item['CharCode']))
    return tuple(result)


def main():
    pass


if __name__ == '__main__':
    main()
