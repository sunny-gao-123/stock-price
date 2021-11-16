class Shares:
    def __init__(self,name,shares,price):
        self.name=name
        self.shares =shares
        self.price=price


class Portfolio:
    def __init__(self):
        self._stocks=[]
    # need to save what have bought somewhere 

    def buy(self,Shares):
        self._stocks.append(Shares)

    def buy_many(self,List_of_stocks):
        for stock in List_of_stocks:
            self.buy(stock)
    
    def cost(self):
        return sum(Shares.shares * Shares.price for Shares in self._stocks)

    def sell(self,stock_name,shares_to_sold):
        # if shares_to_sold is negative --> buy 
        for Stock in self._stocks:
            if Stock.name == stock_name:
                if Stock.shares < shares_to_sold:
                    raise ValueError('do not have enough stocks to sell')
                
                Stock.shares = Stock.shares - shares_to_sold
                break
        else:        
            raise ValueError('you do not own that stock')
 #else: it is executed when the loop terminates through exhaustion of the iterable (with for) 
 #                     but not when the loop is terminated by a break statement


    
