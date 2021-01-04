import json
from datetime import datetime,timedelta
import os

def parse_time(tm):
    datetime.fromisoformat(tm[:-1])

def fix_pairs(p):
    k,v = p
    if k not in ('pickup','dropoff') :
        return p
    return k,parse_time(v)

def pairs_hook(pairs):
    return dict(fix_pairs(pair) for pair in pairs)
    
durations =[]
filepath = os.getcwd()+os.path.sep+'taxi.jl'
print(filepath)
with open(filepath) as fp :
    for l in fp :
        obj = json.loads(l,object_pairs_hook=pairs_hook)
        duration = obj['dropoff'] - obj['pickup']
        durations.append(duration)

avg_dur = sum(durations,timedelta())/len(durations)
print(f'average ride duration: {avg_dur}')
