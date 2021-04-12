import jwt
import uuid
import hashlib
from urllib.parse import urlencode
import json


def order(account_code,price) :
    print("order code :",account_code," price :",price)

order("KRW-EOS",1500)