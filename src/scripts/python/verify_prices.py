import random

import config
from data.pi_symbol_source.pi_symbol_source_utils import get_all_tickers


def verify():
    symbols = [ticker[1] for ticker in get_all_tickers()]

    for symbol in symbols:
        query = f"""
        import "strings"
        from(bucket: "{config.bucket}")
          |> range(start: -40y)
          |> filter(fn: (r) => r._measurement == "public_instruments_data")
          |> filter(fn: (r) => r._field == "price")
          |> filter(fn: (r) => r.symbol == "{symbol}")
          |> filter(fn: (r) => r._value > 0.0)
          |> keep(columns: ["symbol", "_time", "_value"])
        """

        results = config.client.query_api().query(org=config.org, query=query)

        config.log.debug(f"Results recieved for {symbol}: {len(results)}")

        for result in results:
            first_record = result.records[0]
            time_in_first_record = first_record.values['_time']
            symbol_in_first_record = first_record.values['symbol']
            price_in_first_record = first_record.values['_value']
            config.log.debug\
                (f"Symbol={symbol_in_first_record},"
                 f"first date={time_in_first_record},"
                 f"price={price_in_first_record}")

            last_record = result.records[-1]
            time_in_last_record = last_record.values['_time']
            symbol_in_last_record = last_record.values['symbol']
            price_in_last_record = last_record.values['_value']
            config.log.debug(f"Symbol={symbol_in_last_record},"
                             f"first date={time_in_last_record},"
                             f"price={price_in_last_record}")

            rand_int = random.randint(0, len(result.records) - 1)
            random_record = result.records[rand_int]
            time_in_random_record = random_record.values['_time']
            symbol_in_random_record = random_record.values['symbol']
            price_in_random_record = random_record.values['_value']
            config.log.debug \
                (f"Symbol={symbol_in_random_record},"
                 f"first date={time_in_random_record},"
                 f"price={price_in_random_record}")


if __name__ == "__main__":
    verify()