import sys
sys.path.append('./Upbit')

import UpbitApi as Upbit
from UpbitApi import get_info_withdraw

#currency = 'KRW'
#test account info
#Upbit.get_my_account_info()

#test market info
#Upbit.get_order_chance({'market':'KRW-ETH',})

#test ordered info
#Upbit.get_ordered_info({'uuid': '9ca023a5-851b-4fec-9f0a-48cd83c2eaae',})

#test order list
#Upbit.get_order_list(['9ca023a5-851b-4fec-9f0a-48cd83c2eaae',])

#test cancel order
#Upbit.cancel_order({'uuid': 'cdd92199-2897-4e14-9448-f923320408ad',})

#test order bitcoin
# bitcoin = {
#         'market': 'KRW-BTC',
#         'side': 'bid',
#         'volume': '0.01',
#         'price': '100.0',
#         'ord_type': 'limit',
#     }
# Upbit.order_bitcoin(bitcoin)

#테스트 윗드로우 인포
# uid = {
#     'uuid': '9f432943-54e0-40b7-825f-b6fec8b42b79'
# }
# get_info_withdraw(uid)

#test withdraw_list
#withdrawState = {
#    'currency': currency,
#    'state': 'done',
#}
#Upbit.get_info_withdraw_list(withdrawState)

#test withdraw_potential
#Upbit.get_withdraw_potential()
