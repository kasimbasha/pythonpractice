import os
import bz2
import xml.etree.ElementTree as xml
import pandas as pd
# Data conversions
conversion = [
    ('vendor', int),
    ('people', int),
    ('tip', float),
    ('price', float),
    ('pickup', pd.to_datetime),
    ('dropoff', pd.to_datetime),
    ('distance', float),
]

def read_data(fname):
    with bz2.open(fname,'rt') as fp :
        tree = xml.parse(fp)

    rids = tree.getroot()
    for elm in rids :
        rec = {}
        for tag, func in conversion :
            txt = elm.find(tag).text
            rec[tag] = func(txt)
        yield rec

def load_xml(fname):
    rds = read_data(fname)
    return pd.DataFrame.from_records(rds)

def readxmldata():
    filepath = os.getcwd()+os.path.sep+'taxi.xml.bz2'
    rcd = load_xml(filepath)
    print(rcd.dtypes)
    print(rcd.head())


if __name__ == "__main__": readxmldata()