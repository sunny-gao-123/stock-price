class Portfolio:
    def __init__(self):
        self._stocks=[]
    # need to save what have bought somewhere 

    def buy(self,name,shares,price):
        self._stocks.append((name,shares,price))
    
    def cost(self):
        return sum(shares * price for _,shares,price in self._stocks)