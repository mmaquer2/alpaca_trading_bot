
##need to add request package to the file
import request,json
from config import *


##TO DO's and Things to learn:
## 


##URL
baseUrl = "alpaca.com/moneytrader"
accountUrl = ''
secret = secretKey
clientId = clientId
searchUrl = baseUrl + secret + clientId

##get our account

def get_Acnt():
    r = requests.get(searchUrl)


## create an order with the account

def createOrder(symbol,qty,side,time_in_force):
    data = {
        symbol: 'symbol',
        qty: 'qty',
        side:'side',
        time_in_force:'time_in_force'
    }

    r = requests.post(data, json= data)
    return json.loads(r.content)




##create a paper trade order


res = createOrder('MSFT','100','buy','gtc')

print(res)

