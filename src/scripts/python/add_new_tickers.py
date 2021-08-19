from app import create_app
from data.public_instruments.public_instruments_model import PublicInstruments
from config import log
from data.public_instruments.public_instruments_utils import \
    add_to_public_instruments_and_pi_symbol_source
from dtos.public_instrument.addPublicInstrumentDTO import AddPublicInstrumentDTO

TICKERS_TO_ADD = [
    {
        "name": "BinanceCoin ",
        "ticker": "BNB"
    },
    {
        "name": "Solana",
        "ticker": "SOL1"
    },
    {
        "name": "MaticNetwork",
        "ticker": "MATIC"
    },
    {
        "name": "Filecoin",
        "ticker": "FIL"
    },
    {
        "name": "Tezos",
        "ticker": "XTZ"
    },
    {
        "name": "Thorchain",
        "ticker": "RUNE"
    },
    {
        "name": "BasicAttentionToken",
        "ticker": "BAT"
    },
    {
        "name": "InternetComputer",
        "ticker": "ICP1"
    }
]

insert_into_pi_cmd = "insert into public_instruments('symbol', 'name', 'currency', 'is_manual', 'security_type') values('{symbol}', '{name}', '{currency}', '{is_manual}', '{security_type}') ;"


def run():
    for elem in TICKERS_TO_ADD:
        print(elem)
        name = elem['name']
        ticker = elem['ticker']
        existing_pi = PublicInstruments.query.filter_by(symbol=ticker).first()
        if existing_pi is None:
            pi_dto = AddPublicInstrumentDTO(
                name=name,
                currency='USD',
                exchange='',
                security_type='Equity',
                symbol_source='YAHOO-FINANCE',
                symbol=ticker + '-USD',
                is_manual=False,
                description='',
                isin_cusip='None',
                multiplier=1,
                logo=''
            )

            result, log_msg = add_to_public_instruments_and_pi_symbol_source(
                pi_dto, True)

            log.debug(log_msg)


if __name__ == '__main__':
    app = create_app()
    run()
