#test portfolio using pytest
from portfolio import Portfolio,Shares
import pytest

def test_buy_one_stock():
    p = Portfolio()
    a= Shares("IBM", 100, 176.48)
    p.buy(a)
    assert p.cost() == 17648.0

def test_empty_portfolio():
    p = Portfolio()
    assert p.cost()==0.0

def test_buy_multiple_stocks():
    p = Portfolio()
    a= Shares("IBM", 100, 176.48)
    b= Shares("HPQ", 100, 36.15)
    p.buy(a)
    p.buy(b)
    assert p.cost()==21263.0


#A fixture is a function to create the required initial state. Pytest will find and execute them as needed.
#The fixture is a function decorated with @pytest.fixture. 

@pytest.fixture
def simple_portfolio():
    p = Portfolio()
    a=Shares("MSFT", 100, 27.0)        
    b=Shares("DELL", 100, 17.0)        
    c=Shares("ORCL", 100, 34.0)  
    p.buy_many([a,b,c])
    return p


def test_sell_stock(simple_portfolio):
    simple_portfolio.sell("MSFT", 50)
    assert simple_portfolio.cost()== 6450.0

def test_not_enough(simple_portfolio):
    with pytest.raises(ValueError):
        simple_portfolio.sell("MSFT", 200)

def test_dont_own_it(simple_portfolio):
    with pytest.raises(ValueError):
        simple_portfolio.sell("pmg", 1)