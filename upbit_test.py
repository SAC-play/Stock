import sys
sys.path.append('./Upbit')

import UpbitApi as Upbit

currency = 'KRW'
#test account info
Upbit.get_my_account_info()

#test market info
Upbit.get_order_chance({'market':'KRW-ARDR',})

#test ordered info
Upbit.get_ordered_info({'uuid': '9ca023a5-851b-4fec-9f0a-48cd83c2eaae',})

#test order list
Upbit.get_order_list(['9ca023a5-851b-4fec-9f0a-48cd83c2eaae',])

#test cancel order
Upbit.cancel_order({'uuid': 'cdd92199-2897-4e14-9448-f923320408ad',})

#test order bitcoin
bitcoin = {
        'market': 'KRW-BTC',
        'side': 'bid',
        'volume': '0.01',
        'price': '100.0',
        'ord_type': 'limit',
    }
Upbit.order_bitcoin(bitcoin)

#테스트 윗드로우 인포
uid = {
    'uuid': '9f432943-54e0-40b7-825f-b6fec8b42b79'
}
Upbit.get_info_withdraw(uid)

#test withdraw_list
withdrawState = {
   'currency': currency,
   'state': 'done',
}
Upbit.get_info_withdraw_list(withdrawState)

#test withdraw_potential
Upbit.get_withdraw_potential()

#test withdraw coin
coin = {
        'currency': 'BTC',
        'amount': '0.01',
        'address': '3EusRwybuZUhVDeHL7gh3HSLmbhLcy7NqD',
    }
Upbit.withdraw_coin(coin)

#test withdraw krw
krw = {
    'amount': '10000',
}
Upbit.withdraw_krw(krw)

#test get deposits list
unit = {
    'currency': 'KRW',
}
Upbit.get_deposit_list(unit)

#test get deposit info
uid = {
    'uuid': '94332e99-3a87-4a35-ad98-28b0c969f830',
}
Upbit.get_deposit_info(uid)

#test generate coin address
coin_unit = {
    'currency': 'BTC',
}
Upbit.generate_coin_address(coin_unit)

#test get coin addresses
Upbit.get_coin_address_list()

#test get coin an address
coin = {
    'currency': 'BTC',
}
Upbit.get_coin_address(coin)

#test deposit krw
krw_amount = {
    'amount': '10000',
}
Upbit.deposit_krw(krw_amount)

#test status wallet
Upbit.get_status_wallet()

#test api key list
Upbit.get_api_key_list()

#test get market info
Upbit.get_market_info()

#test get candle info
market_unit = 'KRW-BTC'
time_unit = 'minutes/1'
Upbit.get_candle_info(market_unit,time_unit)
#days
time_unit = 'days'
Upbit.get_candle_info(market_unit,time_unit)
#weeks
time_unit = 'weeks'
Upbit.get_candle_info(market_unit,time_unit)
#months
time_unit = 'months'
Upbit.get_candle_info(market_unit,time_unit)

#test get trade info tick
market_unit = 'KRW-BTC'
Upbit.get_trade_info_tick(market_unit)

#test get market info ticker
markets=["KRW-BTC","KRW-EOS"]
Upbit.get_market_info_ticker(markets)

#test get orderbook info
markets=["KRW-BTC","KRW-EOS"]
Upbit.get_orderbook(markets)