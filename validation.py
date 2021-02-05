from collections import namedtuple
from datetime import date,time
# u have data and u have to validate that againest wheather schema
#define collection type

Record = namedtuple('Record','date snow tmax tmin pgtm')
_missing = object()
def validate_tmp(n,v):
    assert v > -900 ,f'{n} {v} too low'
    assert v < 600 ,f'{n} {v} too high'
def validate_snow(n,v):
    assert v>=0,f' negative {n} - {v}'

validators = [
    ('date',None),
    ('snow',validate_snow),
    ('tmax',validate_tmp),
    ('tmin',validate_tmp),
    ('pgtm',None)
]

def validate(r):
    for attr, valid in validators :
        value = getattr(r,attr,_missing)
        assert value is not _missing,f' missing {attr}'
        if valid :
            valid(attr,value)

data = [
    Record(date(2000, 1, 1), 0, 100,  11, time(13, 37)),
    Record(date(2000, 1, 2), 0, 156,  61, time(23, 13)),
    Record(date(2000, 1, 3), 0, 178, 106, time(3,  20)),
    Record(date(2000, 1, 4), 0, 156,  78, time(18, 19)),
    Record(date(2000, 1, 5), 0,  83,  17, time(8,  43)),
]

for r in data :
    validate(r)