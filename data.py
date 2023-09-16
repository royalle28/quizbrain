import requests


request = requests.get('http://localhost:3490/v1/account-totals').json()
keys = request['keys']
clicks = request['clicks']
rank_uptime = request['ranks']['rank_uptime']

print("Current keys: {}, current clicks: {}, rank in uptime: {}".format(keys,
clicks, rank_uptime))