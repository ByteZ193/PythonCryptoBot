BITMEX_MULTIPLIER = 0.00000001

class Balance:
    def __init__(self, info, exchange):
        if exchange == "binance":
            self.initial_margin = float(info['initialMargin']) * BITMEX_MULTIPLIER
            self.maintenance_margin = float(info['maintMargin']) * BITMEX_MULTIPLIER
            self.margin_balance = float(info['marginBalance']) * BITMEX_MULTIPLIER
            self.wallet_balance = float(info['walletBalance']) * BITMEX_MULTIPLIER
            self.unrealized_pnl = float(info['unrealizedProfit']) * BITMEX_MULTIPLIER

        if exchange == "bitmex":
            self.initial_margin = info['initMargin']
            self.maintenance_margin = info['maintMargin']
            self.margin_balance = info['marginBalance']
            self.wallet_balance = info['walletBalance']
            self.unrealized_pnl = info['unrealisedPnl']

class Candle:
    def __init__(self, candle_info, exchange):
        if exchange == "binance":
            self.timestamp = candle_info[0]
            self.open = float(candle_info[1])
            self.high = float(candle_info[2])
            self.low = float(candle_info[3])
            self.close = float(candle_info[4])
            self.volume = float(candle_info[5])

        if exchange == "bitmex":
            self.timestamp = candle_info['timestamp']
            self.open = candle_info['open']
            self.high = candle_info['high']
            self.low = candle_info['low']
            self.close = candle_info['close']
            self.volume = candle_info['volume']

class Contract:
    def __init__(self, contract_info, exchange):
        if exchange == "binance":
            self.symbol = contract_info['symbol']
            self.base_assets = contract_info['baseAsset']
            self.quote_asset = contract_info['quoteAsset']
            self.price_decimals = contract_info['pricePrecision']
            self.quantity_decimals = contract_info['quantityPrecision']

        if exchange == "bitmex":
            self.symbol = contract_info['symbol']
            self.base_assets = contract_info['rootSymbol']
            self.quote_asset = contract_info['quoteCurrency']
            self.price_decimals = contract_info['tickSize']
            self.quantity_decimals = contract_info['lotSize']


class OrderStatus:
    def __init__(self, order_info, exchange):
        if exchange == "binance":
            self.order_id = order_info['orderId']
            self.status = order_info['status']
            self.avg_price = float(order_info['avgPrice'])

        if exchange == "bitmex":
            self.order_id = order_info['orderID']
            self.status = order_info['ordStatus']
            self.avg_price = order_info['avgPx']