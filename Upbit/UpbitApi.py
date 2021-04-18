import jwt
import uuid
import hashlib
from urllib.parse import urlencode
import json
import requests

access_key = "4IRo5Bzmab715nErzjruH8rDqJIeUtGsg4WgWJxe"
secret_key = "BmP2xBSSxZySchtxxUQpRxZ8xxQOIRJDw2FvrHf3"
server_url = "https://api.upbit.com"

def get_my_account_info():
    payload = {
        'access_key': access_key,
        'nonce': str(uuid.uuid4()),
    }

    jwt_token = jwt.encode(payload, secret_key)
    authorize_token = 'Bearer {}'.format(jwt_token)
    headers = {"Authorization": authorize_token}

    res = requests.get(server_url + "/v1/accounts", headers=headers)
    with open('Upbit/output/account_info.json', 'w') as f: 
        json.dump(res.json(), f,indent=4)

    print(res.json())

def get_order_chance(list_market):
    query = list_market
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
    with open('Upbit/output/market_info.json', 'w') as f:
        json.dump(res.json(), f,indent=4)
    print(res.json())

def get_ordered_info(id):
    query = id
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

    res = requests.get(server_url + "/v1/order", params=query, headers=headers)
    with open('Upbit/output/ordered_info.json', 'w') as f:
        json.dump(res.json(), f,indent=4)
    print(res.json())

def get_order_list(ids):
    query = {
        'state': 'done',
    }
    query_string = urlencode(query)

    uuids = ids
    uuids_query_string = '&'.join(["uuids[]={}".format(uuid) for uuid in uuids])

    query['uuids[]'] = uuids
    query_string = "{0}&{1}".format(query_string, uuids_query_string).encode()

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

    res = requests.get(server_url + "/v1/orders", params=query, headers=headers)
    with open('Upbit/output/order_list.json', 'w') as f:
        json.dump(res.json(), f,indent=4)
    print(res.json())

def cancel_order(uuids):
    query = uuids
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

    res = requests.delete(server_url + "/v1/order", params=query, headers=headers)
    with open('Upbit/output/cancel_order.json', 'w') as f:
        json.dump(res.json(), f,indent=4)

    print(res.json())

def order_bitcoin(bitcoin):
    query = bitcoin
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

    res = requests.post(server_url + "/v1/orders", params=query, headers=headers)

def get_info_withdraw(uid):
    query = uid
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

    res = requests.get(server_url + "/v1/withdraw", params=query, headers=headers)
    with open('Upbit/output/get_info_withdraw.json', 'w') as f:
        json.dump(res.json(), f,indent=4)

    print(res.json())
    
def get_info_withdraw_list(withdrawState):
   
    query = withdrawState
    query_string = urlencode(query)

    txids = [
        '98c15999f0bdc4ae0e8a-ed35868bb0c204fe6ec29e4058a3451e-88636d1040f4baddf943274ce37cf9cc',
        #...
    ]
    txids_query_string = '&'.join(["txids[]={}".format(txid) for txid in txids])

    query['txids[]'] = txids
    query_string = "{0}&{1}".format(query_string, txids_query_string).encode()

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

    res = requests.get(server_url + "/v1/withdraws", params=query, headers=headers)
    with open('Upbit/output/withdraw_list.json', 'w') as f:
        json.dump(res.json(), f,indent=4)

    print(res.json())

def get_withdraw_potential():
    query = {
        'currency': 'KRW',
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

    res = requests.get(server_url + "/v1/withdraw", params=query, headers=headers)
    with open('Upbit/output/get_info_withdraw.json', 'w') as f:
        json.dump(res.json(), f,indent=4)

    print(res.json())

def withdraw_coin(coin) :
    query = coin
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

    res = requests.post(server_url + "/v1/withdraws/coin", params=query, headers=headers)
    with open('Upbit/output/get_withdraw_coin.json', 'w') as f:
        json.dump(res.json(), f,indent=4)

    print(res.json())

def withdraw_krw(krw):
    query = krw
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

    res = requests.post(server_url + "/v1/withdraws/krw", params=query, headers=headers)
    with open('Upbit/output/withdraw_krw.json', 'w') as f:
        json.dump(res.json(), f,indent=4)

    print(res.json())

def get_deposit_list(unit):
    query = unit
    query_string = urlencode(query)

    txids = [
        '9e37c537-6849-4c8b-a134-57313f5dfc5a',
        #...
    ]
    txids_query_string = '&'.join(["txids[]={}".format(txid) for txid in txids])

    query['txids[]'] = txids
    query_string = "{0}&{1}".format(query_string, txids_query_string).encode()

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

    res = requests.get(server_url + "/v1/deposits", params=query, headers=headers)
    with open('Upbit/output/deposit_list.json', 'w') as f:
        json.dump(res.json(), f,indent=4)

    print(res.json())

def get_deposit_info(uid):
    query = uid
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

    res = requests.get(server_url + "/v1/deposit", params=query, headers=headers)
    with open('Upbit/output/deposit_info.json', 'w') as f:
        json.dump(res.json(), f,indent=4)

    print(res.json())

def generate_coin_address(coin_unit):
    query = coin_unit
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

    res = requests.post(server_url + "/v1/deposits/generate_coin_address", params=query, headers=headers)
    with open('Upbit/output/generate_coin_address.json', 'w') as f:
        json.dump(res.json(), f,indent=4)

    print(res.json())

def get_coin_address_list():
    payload = {
        'access_key': access_key,
        'nonce': str(uuid.uuid4()),
    }

    jwt_token = jwt.encode(payload, secret_key)
    authorize_token = 'Bearer {}'.format(jwt_token)
    headers = {"Authorization": authorize_token}

    res = requests.get(server_url + "/v1/deposits/coin_addresses", headers=headers)
    with open('Upbit/output/get_coin_address_list.json', 'w') as f:
        json.dump(res.json(), f,indent=4)

    print(res.json())

def get_coin_address(coin):
    query = coin
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

    res = requests.get(server_url + "/v1/deposits/coin_address", params=query, headers=headers)
    with open('Upbit/output/get_coin_address.json', 'w') as f:
        json.dump(res.json(), f,indent=4)

    print(res.json())

def deposit_krw(krw_amount):
    query = krw_amount
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

    res = requests.post(server_url + "/v1/deposits/krw", params=query, headers=headers)
    with open('Upbit/output/deposit_krw.json', 'w') as f:
        json.dump(res.json(), f,indent=4)

    print(res.json())

def get_status_wallet():
    payload = {
        'access_key': access_key,
        'nonce': str(uuid.uuid4()),
    }

    jwt_token = jwt.encode(payload, secret_key)
    authorize_token = 'Bearer {}'.format(jwt_token)
    headers = {"Authorization": authorize_token}

    res = requests.get(server_url + "/v1/status/wallet", headers=headers)
    with open('Upbit/output/wallet_status.json', 'w') as f:
        json.dump(res.json(), f,indent=4)

    print(res.json())

def get_api_key_list():
    payload = {
        'access_key': access_key,
        'nonce': str(uuid.uuid4()),
    }

    jwt_token = jwt.encode(payload, secret_key)
    authorize_token = 'Bearer {}'.format(jwt_token)
    headers = {"Authorization": authorize_token}

    res = requests.get(server_url + "/v1/api_keys", headers=headers)
    with open('Upbit/output/api_key_list.json', 'w') as f:
        json.dump(res.json(), f,indent=4)

    print(res.json())

def get_market_info():
    url = server_url + "/v1/market/all"
    querystring = {"isDetails":"false"}
    response = requests.request("GET", url, params=querystring)
    with open('Upbit/output/market_info.json', 'w') as f:
        json.dump(response.json(), f,indent=4)

    print(response.text)

def get_candle_info(market_unit,time_unit):
    querystring={"market":[],"count":[]}
    querystring["market"] = market_unit
    querystring["count"] = "1"
    url = server_url + "/v1/candles/" + time_unit

    response = requests.request("GET", url, params=querystring)
    time_unit_str = time_unit.replace('/','_')
    file_name = 'Upbit/output/candle_info('+ time_unit_str+ ').json'
    with open(file_name, 'w') as f:
        json.dump(response.json(), f,indent=4)

    print(response.text)

def get_trade_info_tick(market_unit):
    url =  server_url +"/v1/trades/ticks"
    querystring = {"market":"KRW-BTC","count":"1"}
    response = requests.request("GET", url, params=querystring)
    with open('Upbit/output/trade_info_tick.json', 'w') as f:
        json.dump(response.json(), f,indent=4)

    print(response.text)

def get_market_info_ticker(markets):
    url = server_url + "/v1/ticker"
    querystring={"markets":[]}
    querystring["markets"]=markets
    response = requests.request("GET", url,params=querystring)
    with open('Upbit/output/market_info_ticker.json', 'w') as f:
        json.dump(response.json(), f,indent=4)

    print(response.text)

def get_orderbook(markets):
    url = server_url + "/v1/orderbook"
    querystring={"markets":[]}
    querystring["markets"]=markets
    response = requests.request("GET", url,params=querystring)
    with open('Upbit/output/orderbook.json', 'w') as f:
        json.dump(response.json(), f,indent=4)

    print(response.text)