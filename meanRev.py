import request
from config import *

## Trading Bot
class tradingBot(symbol,qty):
    def __init__(self):
        self.symbol = symbol
        self.qty = qty
        self.marketClose = "1600"
    def dataStream(self,prevClose,openPrice,weekLo,weekHi,weekAvg,monthAvg,yearAvg):
        data = {
            prevClose:'',
            openPrice:'',
            weekLo:'',
            weekHi:'',
            weekAvg:'',
            monthAvg:'',
            yearAvg:'',
        }
        stream = request.get(alphavantageUrl + data.json)
        print(stream)
## BUY SIDE ALGO
    if(stream.prevClose < data.yearAvg):
        executeBuyOrder(symbol)
    elif(data.prevClose < data.weekLo & data.monthAvg ):
        executeBuyOrder(symbol)
    elif(crntTime == marketClose):
         executeSellOrder(self)
    
    def executeBuyOrder(self):
        r = requests.post(self, json= data)
        return json.loads(r.content)

    def executeSellOrder(self):
        r = requests.post(self, json= data)
        return json.loads(r.content)
    def marketClose():
        if(crnt time == marketclose):
            executeSellOrder(self)

## run the function based on your inputs

start = tradingBot('MSFT', '100')
start.run()