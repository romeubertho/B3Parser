import io
import os
import zipfile
import csv
import marketdata
import datetime
from b3constants import *

futpath = os.getcwd()+'/data/futures/'
stockpath = os.getcwd()+'/data/stocks/'
optionspath = os.getcwd()+'/data/options'
headers = ['Session Date',
           'Instrument Symbol',
           'Trade Number',
           'Trade Price',
           'Traded Quantity',
           'Trade Time',
           'Trade Indicator',
           'Buy Order Date',
           'Sequential Buy Order Number',
           'Secondary Order ID - Buy Order',
           'Aggressor Buy Order Indicator',
           'Sell Order Date',
           'Sequential Sell Order Number',
           'Secondary Order ID - Sell Order',
           'Aggressor Sell Order Indicator',
           'Cross Trade Indicator',
           'Buy Member',
           'Sell Member']


class B3Parser:
    md = marketdata.MarketData()

    def get_futures(self, date_start, date_end=None, symbol=None):
        print(str(date_start))
        dstart = datetime.datetime.strptime(str(date_start), '%Y%m%d')
        dend = None
        if date_end != None:
            dend = datetime.datetime.strptime(
                str(date_end), '%Y%m%d')+datetime.timedelta(days=1)  # soma um dia
        if dend != None:
            while dstart < dend:
                self.md.get_futures(date=dstart.strftime('%Y%m%d'))
                self.extract(dstart.strftime('%Y%m%d'), symbol)
                dstart = dstart+datetime.timedelta(days=1)  # soma um dia

    def extract(self, date, symbol):
        name = None
        if os.path.exists(futpath+b3TRADE+date+'.zip') is False:
            print("File does not exist!")
            return -1
        zf = zipfile.ZipFile(futpath+b3TRADE+date+'.zip')
        name = zf.namelist()[0]
        print(name)
        zf.extract(name, futpath)
        zf.close()
        if symbol != None:
            with open(futpath+name, 'r') as f:
                head = next(f).split()
                tradingRows = int(head[4].lstrip('0'))
                print(tradingRows)
                md = csv.DictReader(f, delimiter=';', fieldnames=headers)
                line = 2
                try:
                    os.stat(futpath+'/'+symbol)
                except:
                    os.mkdir(futpath+'/'+symbol)
                with open(futpath+'/'+symbol+'/'+date,'w') as out:
                    writer = csv.DictWriter(out, delimiter=';', extrasaction='ignore', fieldnames=headers)
                    writer.writeheader()
                    for row in md:
                        if line < tradingRows:
                            if symbol in row['Instrument Symbol']:
                                row['Instrument Symbol']=row['Instrument Symbol'].strip()
                                row['Trade Number']=row['Trade Number'].lstrip('0')
                                row['Trade Price']=row['Trade Price'].lstrip().lstrip('0')
                                row['Traded Quantity']=row['Traded Quantity'].lstrip('0')
                                row['Sequential Buy Order Number']=row['Sequential Buy Order Number'].lstrip('0')
                                row['Secondary Order ID - Buy Order']=row['Secondary Order ID - Buy Order'].lstrip('0')
                                row['Sequential Sell Order Number']=row['Sequential Sell Order Number'].lstrip('0')
                                row['Secondary Order ID - Sell Order']=row['Secondary Order ID - Sell Order'].lstrip('0')
                                row['Buy Member']=row['Buy Member'].lstrip('0')
                                row['Sell Member']=row['Sell Member'].lstrip('0')
                                writer.writerow(row)
                                # print(row['Instrument Symbol'])
                        line += 1
            f.close()
            os.remove(futpath+name)

    def run(self):
        pass

    if __name__ == '__main__':
        run()

# l = list()
# l2=list()
# tuple = {}


# def test(data):
#     zf = zipfile.ZipFile(futpath+b3TRADE+data+'.zip')
#     name = zf.namelist()[0]
#     zf.extract(name, futpath)
#     zf.close()
#     with open(futpath+name, 'r') as f:
#         head = next(f).split()
#         tradingRows = int(head[4].lstrip('0'))
#         print(tradingRows)
#         md = csv.DictReader(f, delimiter=';', fieldnames=headers)
#         line = 2
#         for row in md:
#             if line % 1000 == 0:
#                 print(line, " - ", row['Instrument Symbol'])
#             if line < tradingRows:
#                 if row['Buy Member'].lstrip('0') not in l:
#                     l.append(row['Buy Member'].lstrip('0'))
#                 if row['Sell Member'].lstrip('0') not in l:
#                     l.append(row['Sell Member'].lstrip('0'))
#                 if (row['Buy Member'].lstrip('0'), row['Instrument Symbol'].strip()) not in l2:
#                     l2.append({row['Buy Member'].lstrip(
#                         '0'), row['Instrument Symbol'].strip()})
#                 if (row['Sell Member'].lstrip('0'), row['Instrument Symbol'].strip()) not in l2:
#                     l2.append({row['Sell Member'].lstrip(
#                         '0'), row['Instrument Symbol'].strip()})
#                 # if row['Instrument Symbol'].strip() == 'WDOG18':
#                     # print(row['Buy Member'].lstrip('0'), " -- ",
#                     #       row['Traded Quantity'].lstrip('0'), " -- ", row['Sell Member'].lstrip('0'))
#             line += 1


# test('20180102')
# print(l)
# print(l2)
