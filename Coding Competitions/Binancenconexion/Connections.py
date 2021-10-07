from binance import  Client, ThreadedWebsocketManager, ThreadedDepthCacheManager

binance_keys = {
	'api_key': "19gFZB9lGiU9ici9kbBavBRWKBykd5j34t8c55dFZpPvFniS3eZlJrYe8tHxETrC",
	'secret_key': "bfwFZCmgWAIHGDfM2U1ZsmRkMDygRzsFkZBnZPU1X53SwRYJzaGdxCo8vbowVrLU"
}

def __init__(self):
    self.base = 'https://api.binance.com'
    self.endpoints = {
        "order": '/api/v3/order',
        "testOrder": '/api/v3/order/test',
        "allOrders": '/api/v3/allOrders',
        "klines": '/api/v3/klines',
        "exchangeInfo": '/api/v3/exchangeInfo'
    }



def Main():
    client = Client(binance_keys['secret_key'], binance_keys['api_secret'])
    prices = client.get_exchangeInfo()

    for pair in prices:
        print(pair)


if __name__ == '__main__':
    Main()