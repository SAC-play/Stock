# import pyupbit
# print(pyupbit.Upbit)

# # tickers = pyupbit.get_tickers(fiat="KRW")
# # print(tickers)

# # price = pyupbit.get_current_price("KRW-XRP")
# # print(price)

# # price = pyupbit.get_current_price("BTC-XRP")
# # print(price)

# price = pyupbit.get_current_price(["KRW-EOS"])
# print(price)

# # df = pyupbit.get_ohlcv("KRW-BTC")
# # print(df)

# access_key = "fdmjDOKz3gze0ZCPHmkbynR0FC1STwKQiuKvTy9o"
# secret_key = "0BfVgaJUGsXqEyByGowjxq4kboECKKO1Fp4UVumS"

# ##check your blance in bitcoin
# upbit = pyupbit.Upbit(access_key, secret_key)
# print(upbit.get_balances())

# orderbook = pyupbit.get_orderbook("KRW-EOS")
# print(orderbook)

import os
import jwt
import uuid
import hashlib
from urllib.parse import urlencode

import requests
import json

access_key = "fdmjDOKz3gze0ZCPHmkbynR0FC1STwKQiuKvTy9o"
secret_key = "0BfVgaJUGsXqEyByGowjxq4kboECKKO1Fp4UVumS"
server_url = "https://api.upbit.com"

payload = {
    'access_key': access_key,
    'nonce': str(uuid.uuid4()),
}

jwt_token = jwt.encode(payload, secret_key)
authorize_token = 'Bearer {}'.format(jwt_token)
headers = {"Authorization": authorize_token}

res = requests.get(server_url + "/v1/accounts", headers=headers)
with open('output/account_info.json', 'w') as f:
    json.dump(res.json(), f,indent=4)

print(res.json())
print()

query = {
    'market': 'KRW-EOS',
}
query_string = urlencode(query).encode()

m = hashlib.sha512()
m.update(query_string)
query_hash = m.hexdigest()

payload = {
    'access_key': access_key,
    'nonce': str(uuid.uuid4()),
    'query_hash': query_hash,
    'query_hash_alg': 'SHA512',
}

jwt_token = jwt.encode(payload, secret_key)
authorize_token = 'Bearer {}'.format(jwt_token)
headers = {"Authorization": authorize_token}

res = requests.get(server_url + "/v1/orders/chance", params=query, headers=headers)
with open('output/market_info.json', 'w') as f:
    json.dump(res.json(), f,indent=4)

print(res.json())