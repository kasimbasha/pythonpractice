import os
import csv
import bz2
from collections import namedtuple
from datetime import datetime
import json
#read csv 
clm = namedtuple('Column','src dest convert')
def parse_timestamp(v):
    datetime.strptime(v,'%Y-%m-%d %H:%M:%S')

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
def itr_reader(filename):
    with bz2.open(filename,"rt") as fp :
        r = csv.DictReader(fp)
        for c in r :
            rcd = {}
            for cc in colms :
                value = c[cc.src]
                rcd[cc.dest] = cc.convert(value)
            yield rcd
# write into json object
def encode_time(obj) :
    if not isinstance(obj,datetime):
        return obj
    return obj.isoformat()

def test():
    jsonfile = os.getcwd()+os.path.sep+'taxi1.jl'
    with open(jsonfile,'w') as out:
        csvfile= os.getcwd()+os.path.sep+'taxi.csv.bz2'
        for r in itr_reader(csvfile):
            data = json.dumps(r,default=encode_time)
            out.write(f'{data}\n')

if __name__ == "__main__": test()