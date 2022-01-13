import tkinter as tk
import logging
from tkinter import font
from tkinter.constants import EW, PIESLICE
from conectors.binance_futures import BinanceFuturesClinet
from conectors.bitmex import BitmexClinet
from interface.root_component import Root

logger = logging.getLogger()

logger.setLevel(logging.DEBUG)

stream_handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s %(levelname)s :: %(message)s')
stream_handler.setFormatter(formatter)
stream_handler.setLevel(logging.INFO)

file_handler = logging.FileHandler('info.log')
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.DEBUG)

logger.addHandler(stream_handler)
logger.addHandler(file_handler)

"""
logger.debug("This message is important only when debugging the program")
logger.info("This message just shows basic information")
logger.warning("This message is about something you should pay attention to")
logger.error("This message helps to debugan error that occurred in your program")
"""


if __name__ == '__main__':

    binance = BinanceFuturesClinet("6558cee30361def71f9d7ae147870a0e6cec98f7bca52fbaf360d5481ab63580", "0889dfba638f3b2a314d1bc320954be8b46f4078a83a3ad2ded09bdc58290704", True)
    # print(binance.get_balances())
    # print(binance.place_order("BTCUSDT", "BUY", 0.01, "LIMIT", 20000, "GTC"))
    # print(binance.get_order_status("BTCUSDT", 2728938950))
    # print(binance.cancel_order("BTCUSDT", 2729677482))

    bitmex = BitmexClinet("JVI8VsHv6vt3fIN9BGI1J3WR", "qV8DIZv1CtZQWngAaNtB8WfWEdDfvyB-XWbz7g99lPj1h0H4", True)

    # print(bitmex.get_order_status("8212f0d1-21df-4d8d-9059-2ecbb09f32a6", bitmex.contracts['XBTUSD']).status)
    # print(bitmex.cancel_order("8212f0d1-21df-4d8d-9059-2ecbb09f32a6").status)
    # bitmex.get_historical_candles(bitmex.contracts['XBTUSD'], "1h")
    # print(bitmex.place_order(bitmex.contracts['XBTUSD'], "Limit", 100, "Buy", 20000.3987667, "GoodTillCancel"))

    root = Root()
    root.mainloop()
