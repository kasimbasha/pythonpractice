# use https://pythex.org/ to check regex online
import re
from datetime import datetime
import os
import bz2
import logging


def parse_line(line):
    # Example:  Ride of 1 passenger started at 2018-10-31T07:10:55 and paid $20.54
    mt = re.search(r'(\d+).*started at ([^ ]+).*paid \$(\d+\.\d+)',line)
    if not mt:
        return None
    return {
        'count':int(mt.group(1)),
        'start' : datetime.fromisoformat(mt.group(2)),
        'amount':float(mt.group(3))
    }

def itr_rec(f):
    with bz2.open(f,'rt') as fp :
        for l,line in enumerate(fp,1):
            rcd = parse_line(line)
            if not rcd :
                logging.warning(f'{l} cannot parse line')
            yield rcd

if __name__ == "__main__":
    from pprint import pprint
    filepath = os.getcwd()+os.path.sep+'taxi.log.bz2'
    for i,rides in enumerate(itr_rec(filepath)):
        if i>5 :
            break
        pprint(rides)