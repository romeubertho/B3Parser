"""A MarketData class responsible to download only B3 futures, options and stocks data.

by Romeu Bertho Junior

Example:

>>> import marketdata
>>> md=marketdata.MarketData()
>>> md.get_futures(date='20180102') # download futures marketdata
"""
import os
import ftplib
from b3constants import *


class MarketData:
    ftp = None
    # Initialization method (called by class instantiation).

    def __init__(self):
        self.ftp = ftplib.FTP(b3URL)
        self.ftp.login()

    def get_futures(self, date, path=os.getcwd()):
        self.ftp.cwd('../')
        self.ftp.cwd(b3FUTURES)
        filename = b3TRADE+date+'.zip'
        print('Downloading',filename)
        path +='/data/futures/'+filename
        filesFTP=self.ftp.nlst()
        if filename in filesFTP:
            res = self.ftp.retrbinary("RETR " + filename, open(path, 'wb').write)
            print(res)
        else:
            print(filename,'not found!')

    def get_options(self, date=''):
        pass

    def get_stocks(self, date=''):
        pass
    
    def run(self):
        pass
    
    if __name__ == '__main__':
        run()
