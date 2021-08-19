from datetime import datetime, timedelta
from itertools import product

import yfinance
from dateutil.relativedelta import relativedelta

from app import create_app
from psql import Symbol
import pandas as pd

CONVERSION_CURRENCY = "USD"

CRYPTOS = (
    'DOGE',
    'ETH',
    'LINK',
    'LTC',
    'ADA',
    'XMR',
    'UNI',
    'BTC',
    'XRP',
    'DOT1'
)

NATIONAL_CURRENCIES = (
    'HKD',
    'CNY',
    'SGD',
    'SEK',
    'AUD',
    'JPY',
    'GBP',
    'INR',
    'CHF',
    'BTC',
    'RUB',
    'CAD',
    'KRW',
    'BRL',
    'AED',
    'EUR',
    'ZAR',
    'USD'
)


def get_crypto_list():
    cartesian_product_crypto = product(CRYPTOS, NATIONAL_CURRENCIES)
    forward = list(map(','.join, cartesian_product_crypto))
    tickers_list = forward
    # Do the same thing for reverse pairs
    cartesian_product_crypto = product(NATIONAL_CURRENCIES, CRYPTOS)
    reverse = list(map(','.join, cartesian_product_crypto))
    tickers_list += reverse

    return tickers_list


def check_pair_exists_in_yfinance(source, dest):
    currency_str = f"{source}{dest}"

    if source in CRYPTOS or dest in CRYPTOS:
        currency_str = f"{source}-{dest}"

    reverse_conversion_record = yfinance.download(
        [f"{currency_str}"],
        start=datetime.now() - relativedelta(days=1))['Close']
    if len(reverse_conversion_record) > 0:
        return True

    return False


def generate_qstring_crypto():

    symbol_perms = get_crypto_list()
    conversions = {k: '' for k in symbol_perms}
    for symbol in symbol_perms:
        source, dest = symbol.split(',')

        if source == dest:
            continue

        if check_pair_exists_in_yfinance(source, dest):
            currency_str = f"{source}{dest}"
            if source in CRYPTOS or dest in CRYPTOS:
                currency_str = f"{source}-{dest}"
            conversions[f"{source}{dest}"] = currency_str
            continue

        # If this pair doesn't exist in YAHOO-FINANCE
        else:
            # Find a conversion

            # here we check for conversions in each of the convertable currencies
            # record_in_db = None
            # currency_str = None
            # conversion_currency = None
            # for int_currency in intermediate_currency_order:
            #     conversion_currency = int_currency
            #     currency_str = f"{source}{int_currency}"
            #     record_in_db = all_symbols_df[
            #         all_symbols_df.symbol == currency_str]
            #
            #     if len(record_in_db) > 0:
            #         break

            conversion = None
            # Eg: DOGE,EUR
            if source in CRYPTOS and dest not in CRYPTOS:
                conversion = f"{source}-{CONVERSION_CURRENCY}*{CONVERSION_CURRENCY}{dest}=X"

            # Eg: EUR,DOGE
            if source not in CRYPTOS and dest in CRYPTOS:
                if source == 'USD':
                    conversion = f"1/{dest}-{source}"

                else:
                    # IF a reverse conversion exists:
                    # We check yfinance if a reverse symbol exists
                    reverse_string = f"{dest}-{source}"
                    reverse_conversion_record = yfinance.download(
                        [reverse_string],
                        start=datetime.now() - relativedelta(days=1))['Close']

                    if len(reverse_conversion_record):
                        conversion = f"1/{reverse_string}"
                    else:
                        conversion = f"{source}{CONVERSION_CURRENCY}=X/{dest}-{CONVERSION_CURRENCY}"

            # Eg: DOGE,USD
            if source in CRYPTOS and dest in CRYPTOS:
                conversion = f"{source}-USD/{dest}-USD"

            if dest not in CRYPTOS and source not in CRYPTOS:
                conversion = f"{source}USD=X*USD{dest}"

            #TODO: If source AND dest in cryptos

            conversions[f"{source},{dest}"] = conversion

    return conversions


def build_insert_query(conversion_dict):
    all_queries = []

    symbols_query = Symbol.query.filter(Symbol.symbol is not None)
    all_symbols_df = pd.read_sql(
        symbols_query.statement, symbols_query.session.bind)
    for k, v in conversion_dict.items():
        symbol = k.replace(',', '')
        qstring = v

        if qstring:
            existing_record = all_symbols_df[all_symbols_df.symbol == symbol]
            if len(existing_record) > 0:
                query = f"update symbol set qstring = '{qstring}' where symbol = '{symbol}';"
            else:
                query = f"insert into symbol (symbol, qstring) values ('{symbol}','{qstring}');"

            all_queries.append(query)

    return all_queries


if __name__ == "__main__":
    app = create_app()

    with app.app_context():
        d = generate_qstring_crypto()
        for q in build_insert_query(d):
            print(q)
