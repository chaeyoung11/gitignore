import pprint
import requests

r=requests.get('http://api.github.com/users/chaeyoung11')

if r.status_code==200:
    json_data=r.json()
    pprint.pprint(json_data)

