from datetime import datetime
from urllib.request import urlopen
import json

def user_req_tim(uname):
    url = 'https://api.github.com/users/'+uname
    resp = urlopen(url)
    rply = json.load(resp)
    loginName = rply['login']
    ts = rply['created_at']
    createdDate = datetime.fromisoformat(ts[:-1])
    print(createdDate)
    return loginName

login = 'kasimbasha'
print(user_req_tim(login))