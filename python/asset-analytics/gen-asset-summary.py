import pandas as pd
import numpy as np
from os import listdir
from tabulate import tabulate
from os.path import isfile, join
from datetime import datetime
import logging

logging.basicConfig()
logger = logging.getLogger("trade-summary")
logger.setLevel(logging.DEBUG)

my_dir = r'D:\database\users\vishal\assets\asset-summary\zerodha'
filter_sym = 'CUB'
filter_sym = 'HINDZINC'


class Helper:
    @staticmethod
    def convert_datetime(date_str, date_fmt):
        return datetime.strptime(date_str, date_fmt)

    @staticmethod
    def get_file_list(dir):
        """
        Get files in dir.
        :param dir:
        :return:
        """
        return [(lambda f: join(my_dir, f))(f) for f in listdir(dir)]

    @staticmethod
    def read_csv(file_list):
        """
        Convert csv to dataframe.
        :param file_list:
        :return:
        """
        df_list = []
        # Read csv as df
        for f in file_list:
            df_list.append(pd.read_csv(f))

        return pd.concat(df_list, axis=0)

    @staticmethod
    def print_pretty(df):
        """
        Print pretty
        :param df:
        :return:
        """
        print(tabulate(df, headers='keys', tablefmt='psql'))


class Constants:
    symbol = 'symbol'
    trade_type = 'trade_type'
    trade_date = 'trade_date'
    buy_date = 'buy_date'
    sell_date = 'sell_date'
    quantity = 'quantity'
    price = 'price'

class TradeSummary:
    """
    TradeSummary class
    """

    @staticmethod
    def get_trades(df, trade_type, symbol=None):

        df1 = None
        if symbol is None:
            df1 = df.loc[(df[Constants.trade_type].isin([trade_type]))]
        else:
            df1 = df.loc[(df[Constants.trade_type].isin([trade_type])) & (df[Constants.symbol].isin([symbol]))]

        # set date
        df1[Constants.trade_date] = pd.to_datetime(df1[Constants.trade_date], format='%Y-%m-%d')

        result = df1.groupby([Constants.symbol, Constants.trade_date]).agg(
            {Constants.quantity: np.sum, Constants.price: [np.min]})

        result.columns = list(map("_".join, result.columns))

        result.reset_index(inplace=True)
        result.rename(columns={'quantity_sum': trade_type + '_quantity', 'price_amin': trade_type + '_price', Constants.trade_date: trade_type + '_date'},
                      inplace=True)

        logger.debug("result {}".format(result))

        return result

    @staticmethod
    def summarize(df):
        buy_df = TradeSummary.get_trades(df, 'buy', filter_sym)


        for row in buy_df.itertuples():
            logger.debug(row)


        sell_df = TradeSummary.get_trades(df, 'sell', filter_sym)
        # Join
        # merged = pd.merge(buy_df, sell_df, on='symbol', how='left')
        # merged['diff'] = merged[Constants.buy_date] - merged[Constants.sell_date]
        # merged.sort_values([Constants.buy_date, Constants.symbol], ascending=[True, False], inplace=True)


# -------------------------
# Main
# -------------------------
file_list = Helper.get_file_list(my_dir)
df = Helper.read_csv(file_list)
ts = TradeSummary()
result = ts.summarize(df)
Helper.print_pretty(result)
