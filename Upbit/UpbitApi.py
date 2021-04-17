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