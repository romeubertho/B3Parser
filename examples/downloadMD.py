import sys
import os
sys.path.insert(0,os.getcwd()+"/src")
import marketdata
import b3parser
'''
Download 1 day of all market data available 
and stores it in ../data folder 
'''
# md=marketdata.MarketData()
#Download futures trading data
# md.get_futures(date='20180101')
#Download futures orderbook data
#Download options trading data
# md.get_options(date='20180102')
#Download options orderbook data
#Download stocks trading data
# md.get_stocks(date='20180102')
#Download stocks orderbook data

b3=b3parser.B3Parser()
b3.get_futures('20180101','20180131','WDO')