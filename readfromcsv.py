import os
import bz2
import csv
from collections import namedtuple
from datetime import datetime

clm = namedtuple('Column','src dest convert')

def parse_timestamp(txt):
    return datetime.strptime(txt,'%Y-%m-%d %H:%M:%S')

colms =[
    clm('VendorID','vendor_id',int),
    clm('passenger_count','num_passengers',int),
    clm('tip_amount','tip',float),
    clm('tpep_dropoff_datetime', 'dropoff_time', parse_timestamp),
    clm('tpep_pickup_datetime', 'pickup_time', parse_timestamp),
    clm('trip_distance', 'distance', float),
    clm('RatecodeID', 'rate_code', int),
    clm('store_and_fwd_flag', 'flag', str),
]

def iter_records(f):
    with bz2.open(f,'rt') as fp:
        r = csv.DictReader(fp)
        for c in r:
            rcd ={}
            for cc in colms :
                v = c[cc.src]
                rcd[cc.dest] = cc.convert(v)
            yield rcd

def test():
    filepath = os.getcwd()+os.path.sep+'taxi.csv.bz2'
    print(filepath)
    from pprint import pprint
    for i,record in enumerate(iter_records(filepath)):
        if i>=10:
            break
        pprint(record)




if __name__ == "__main__": test()