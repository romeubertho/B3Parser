import io
import os
import zipfile
import csv
from b3constants import *

futpath = os.getcwd()+'/data/futures/'
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


def test(data):
    zf = zipfile.ZipFile(futpath+b3TRADE+data+'.zip')
    name = zf.namelist()[0]
    zf.extract(name, futpath)
    zf.close()
    with open(futpath+name, 'r') as f:
        next(f)
        md = csv.DictReader(f, delimiter=';', fieldnames=headers)
        print(md)
        line=0
        for row in md:
            if line%1000 is 0:
                print(line," - ",row['Instrument Symbol'])
            line+=1
    # datalist=list(teste)
    # print(datalist[0][1])


test('20180102')
