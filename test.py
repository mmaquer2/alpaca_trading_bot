
##need to add request package to the file
##import request,json
from config import *
import alpaca_trade_api as tradeapi


##TO DO's and Things to learn:
    ##how does self work in a class and the scope of inheritance


##URL 
secKey = alpacaaSecKey
clientId = alpacaApiKey

class testBot(secKey,clientId,symbol,qty,side,time_in_force,stop_price,limit_price):
    def __init__(self):
        this.baseUrl = baseUrl
        this.secKey = secKey
        this.clientId = clientId

    def getAccount(self):

        api = tradeapi.REST(alpacaApiKey, secKey, api_version='v2') # or use ENV Vars shown below
        account = api.get_account()
        api.list_positions()

## create an order with the account

    def createOrder(symbol,qty,side,time_in_force):
    api.submit_order(
        symbol='symbol',
        side='qty',
        type='market',
        qty='100',
        time_in_force='day',
        order_class='bracket',
        take_profit=dict(
        limit_price='305.0',
        ),
        stop_loss=dict(
            stop_price='295.5',
            limit_price='295.5',
        )
    )
##create a paper trade order
## secKey,clientId,symbol,qty,side,time_in_force,stop_price,limit_price  
# this is the total args

res = testBot(secKey,clientId,'MSFT','100','buy','gtc','320','380')

print(res)

