import json
from datetime import datetime

data = b'''
{
  "from": "Wile. E. Coyote",
  "to": "ACME",
  "amount": 103.7,
  "time": "2019-08-07T12:28:39.781551"
}
'''

def fix_time(pair):
    k,v = pair
    if k!='time':
        return pair
    return (k,datetime.fromisoformat(v))

def object_pairs_hook(pairs):
    return dict(fix_time(p) for p in pairs)

obj = json.loads(data,object_pairs_hook=object_pairs_hook)
print(obj)