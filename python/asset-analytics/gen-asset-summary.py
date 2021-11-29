import pandas as pd
import numpy as np
from os import listdir
from tabulate import tabulate
from os.path import isfile, join
from datetime import datetime
import logging

logging.basicConfig()
logger = logging.getLogger("trade-summary")
logger.setLevel(logging.INFO)

my_dir = r'D:\database\users\vishal\assets\asset-summary\zerodha'


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
    sell_date = 'sell_date'
    quantity = 'quantity'
    price = 'price'
    buy_date = 'buy_date'
    buy_quantity = 'buy_quantity'
    buy_price = 'buy_price'
    sell_date = 'sell_date'
    sell_quantity = 'sell_quantity'
    sell_price = 'sell_price'
    period = 'period'
    profit = 'profit'
    sold = 'sold'


class Trade:
    """
    Trade represents buy or buy/sell transaction
    Order of elements in tuple => sym,
    """

    def __init__(self, trade_tuple):
        self.symbol = trade_tuple[0]
        self.buy_date = trade_tuple[1]
        self.buy_quantity = trade_tuple[2]
        self.buy_price = trade_tuple[3]
        self.sell_date = trade_tuple[4]
        self.sell_quantity = trade_tuple[5]
        self.sell_price = trade_tuple[6]

    def __str__2(self):
        return "{}:: *** buy [{} {} {}]  *** sell [{} {} {}]".format(self.symbol,
                                                                     self.buy_date, self.buy_quantity, self.buy_price,
                                                                     self.sell_date, self.sell_quantity,
                                                                     self.sell_price)

    def __str__(self):
        return "{},{},{},{},{},{},{}".format(self.symbol,
                                             self.buy_date, self.buy_quantity, self.buy_price,
                                             self.sell_date, self.sell_quantity, self.sell_price)

    def get_field_list(self):
        return [self.symbol,
                self.buy_date, self.buy_quantity, self.buy_price,
                self.sell_date, self.sell_quantity, self.sell_price]


class MultiTrade:
    """Holds all buy/sell transactions per symbol"""

    def __init__(self):
        self.buy_trade_list = None
        self.sell_trade_list = None

    def __str__2(self):
        buy_trades = "\n".join(map(str, self.buy_trade_list))
        sell_trades = "\n".join(map(str, self.sell_trade_list))
        return buy_trades + "\n" + sell_trades

    def __str__(self):
        return "\n".join(map(str, self.buy_trade_list))

    def get_buy_trade_list(self):
        return self.buy_trade_list

    def add_trade_list(self, trade_type, trade_list):
        if trade_type == 'buy':
            self.buy_trade_list = trade_list
        else:
            self.sell_trade_list = trade_list

    def match_buy_sell(self):
        if self.sell_trade_list is None or len(self.sell_trade_list) <= 0:
            return

        b_index = 0
        s_index = 0

        # Iterate thru all buy trades, and adjust buy/sell qty
        while b_index < len(self.buy_trade_list) and s_index < len(self.sell_trade_list):
            logger.info("-------------------------")
            logger.info("...processing buy-trade [{} of {}]]".format(b_index, len(self.buy_trade_list), s_index))
            logger.info("...processing sell-trade [{} of {}]]".format(s_index, len(self.sell_trade_list)))
            if b_index < len(self.buy_trade_list) and s_index < len(self.sell_trade_list):
                logger
            #
            buy_trade = self.buy_trade_list[b_index]
            b_index = b_index + 1

            sell_trade = self.sell_trade_list[s_index]

            logger.debug("BUY ==> {}".format(buy_trade))
            logger.debug("SELL ==> {}".format(sell_trade))

            if buy_trade.buy_quantity <= sell_trade.sell_quantity:
                buy_trade.sell_quantity = buy_trade.buy_quantity
                buy_trade.sell_date = sell_trade.sell_date
                buy_trade.sell_price = sell_trade.sell_price
            else:
                self.clone_buy(b_index - 1, buy_trade.buy_quantity - sell_trade.sell_quantity)
                buy_trade.buy_quantity = sell_trade.sell_quantity
                buy_trade.sell_quantity = sell_trade.sell_quantity
                buy_trade.sell_date = sell_trade.sell_date
                buy_trade.sell_price = sell_trade.sell_price
            sell_trade.sell_quantity = sell_trade.sell_quantity - buy_trade.buy_quantity
            if sell_trade.sell_quantity <= 0:
                s_index = s_index + 1

            logger.debug("...end-of-loop buy-trade [{} of {}]]".format(b_index, len(self.buy_trade_list), s_index))
            logger.debug("...end-of-loop sell-trade [{} of {}]]".format(s_index, len(self.sell_trade_list)))
        self.sell_trade_list = []

    def clone_buy(self, source_index, new_qty):
        logger.debug("request to clone... source_index={}, qty={}".format(source_index, new_qty))
        logger.debug(" *** before cloning buy trades [{}]".format("\n".join(map(str, self.buy_trade_list))))
        trade = self.buy_trade_list[source_index]
        cloned_trade = Trade((trade.symbol,
                              trade.buy_date, new_qty, trade.buy_price,
                              None, None, None))
        self.buy_trade_list.insert(source_index + 1, cloned_trade)
        logger.debug(" *** after cloning buy trades [{}]".format("\n".join(map(str, self.buy_trade_list))))


class TradeHelper:
    """
    TradeHelper class
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
        result.rename(columns={'quantity_sum': trade_type + '_quantity', 'price_amin': trade_type + '_price',
                               Constants.trade_date: trade_type + '_date'},
                      inplace=True)

        logger.debug("result {}".format(result))

        return result

    @staticmethod
    def create_trade(sym, trade_type, trade_df):
        """
        Create Trade list for specified trade_df
        1 to 1.
        :param sym:
        :param trade_type:
        :param trade_df:
        :return:
        """
        tt_list = []
        for trade_row in trade_df.itertuples():
            logger.debug("trade_row = {}".format(trade_row))
            trade_tuple = ()
            if trade_type == "buy":
                trade_tuple = (sym, trade_row.buy_date, trade_row.buy_quantity, trade_row.buy_price, None, None, None)
            else:
                trade_tuple = (
                    sym, None, None, None, trade_row.sell_date, trade_row.sell_quantity, trade_row.sell_price)

            tt = Trade(trade_tuple)
            tt_list.append(tt)

        return tt_list

    @staticmethod
    def summarize(df):
        filter_sym = None
        #filter_sym = 'RITES'
        buy_df = TradeHelper.get_trades(df, 'buy', filter_sym)
        sell_df = TradeHelper.get_trades(df, 'sell', filter_sym)

        # Get unique symbols
        buy_sym_list = buy_df.symbol.unique()
        logger.info("buy symbols : {}".format(buy_sym_list))

        # Process trades per symbol
        all_multi_trade = []
        for sym in buy_sym_list:
            logger.info("------ symbol ----- {}".format(sym))

            #
            sym_buy_df = buy_df[(buy_df['symbol'] == sym)]
            logger.debug("{}:: found {} buy transactions".format(sym, len(sym_buy_df)))

            #
            sym_sell_df = sell_df[(sell_df['symbol'] == sym)]
            logger.debug("{}:: found {} sell transactions".format(sym, len(sym_sell_df)))

            # Create Trade
            multi_trade = MultiTrade()
            multi_trade.add_trade_list("buy", TradeHelper.create_trade(sym, "buy", sym_buy_df))
            multi_trade.add_trade_list("sell", TradeHelper.create_trade(sym, "sell", sym_sell_df))

            multi_trade.match_buy_sell()
            logger.info("{} :: {}".format(sym, multi_trade))
            all_multi_trade.append(multi_trade)

        # Convert to df
        column_names = [Constants.symbol,
                        Constants.buy_date, Constants.buy_quantity, Constants.buy_price,
                        Constants.sell_date, Constants.sell_quantity, Constants.sell_price]

        df = pd.DataFrame(columns=column_names)
        index = 0
        for multi_trade in all_multi_trade:
            for buy_trade in multi_trade.get_buy_trade_list():
                df.loc[index] = buy_trade.get_field_list()
                index = index + 1

        return df

    @staticmethod
    def add_analytics(df):
        """
        Add below analytics.
          * period : If sell has happened,  period = sell_date - buy_date
          *          If sell has not happened,  period = today - buy_date
          * profit : total_sell - total_buy
          * notional : y - if sell has happened
        :param df:
        :return:
        """

        logger.info("Columns in df : {}".format(df.columns.to_list()))
        df[Constants.profit] = df[Constants.sell_quantity] * df[Constants.sell_price] - df[Constants.buy_quantity] * df[
            Constants.buy_price]
        df[Constants.sell_date] = np.where(df[Constants.sell_date].isnull(), datetime.now(), df[Constants.sell_date])
        df[Constants.period] = (df[Constants.sell_date] - df[Constants.buy_date]).dt.days
        df[Constants.sold] = np.where(df[Constants.sell_quantity].isnull(), False, True)


# -------------------------
# Main
# -------------------------
file_list = Helper.get_file_list(my_dir)
df = Helper.read_csv(file_list)
summary_df = TradeHelper.summarize(df)
TradeHelper.add_analytics(summary_df)
Helper.print_pretty(summary_df)
