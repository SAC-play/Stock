import sys
import os
api_dirName=os.path.dirname(os.path.realpath(__file__))+'/../api'
sys.path.append(api_dirName)

import UpbitApi as Upbit
import unittest

class UpbitUnitTest(unittest.TestCase):
    def test_get_my_account_info(self):
        json_data = Upbit.get_my_account_info()
        self.assertTrue('error' not in json_data)

    def test_get_order_chance(self):
        json_data = Upbit.get_order_chance({'market':'KRW-BTC',})
        self.assertTrue('error' not in json_data)
    
    def test_get_ordered_info(self):
        json_data = Upbit.get_ordered_info({'uuid': '9ca023a5-851b-4fec-9f0a-48cd83c2eaae',})
        self.assertTrue('error' not in json_data)

    def test_get_order_list(self):
        json_data = Upbit.get_order_list(['9ca023a5-851b-4fec-9f0a-48cd83c2eaae',])
        self.assertTrue('error' not in json_data)

    def test_cancel_order(self):
        json_data = Upbit.cancel_order({'uuid': 'cdd92199-2897-4e14-9448-f923320408ad',})
        self.assertTrue('error' not in json_data)

    def test_order_bitcoin(self):
        json_data = Upbit.order_bitcoin({
                                                                    'market': 'KRW-BTC',
                                                                    'side': 'bid',
                                                                    'volume': '0.01',
                                                                    'price': '100.0',
                                                                    'ord_type': 'limit',
                                                                })
        self.assertTrue('error' not in json_data)

    def test_get_info_withdraw(self):
        json_data = Upbit.get_info_withdraw({
                                                                            'uuid': '9f432943-54e0-40b7-825f-b6fec8b42b79'
                                                                        })
        self.assertTrue('error' not in json_data)

    def test_get_info_withdraw_list(self):
        json_data = Upbit.get_info_withdraw_list({
                                                                                    'currency': 'KRW',
                                                                                    'state': 'done',
                                                                                })
        self.assertTrue('error' not in json_data)

    def test_get_withdraw_potential(self):
        json_data = Upbit.get_withdraw_potential()
        self.assertTrue('error' not in json_data)

    def test_withdraw_coin(self):
        json_data = Upbit.withdraw_coin({
                                                                    'currency': 'BTC',
                                                                    'amount': '0.01',
                                                                    'address': '3EusRwybuZUhVDeHL7gh3HSLmbhLcy7NqD',
                                                                })
        self.assertTrue('error' not in json_data)
    
    def test_withdraw_krw(self):
        json_data = Upbit.withdraw_krw({
                                                                    'amount': '10000',
                                                                })
        self.assertTrue('error' not in json_data)

    def test_get_deposit_list(self):
        json_data = Upbit.get_deposit_list({
                                                                        'currency': 'KRW',
                                                                    })
        self.assertTrue('error' not in json_data)

    def test_get_deposit_info(self):
        json_data = Upbit.get_deposit_info({
                                                                            'uuid': '94332e99-3a87-4a35-ad98-28b0c969f830',
                                                                        })
        self.assertTrue('error' not in json_data)

    def test_generate_coin_address(self):
        json_data = Upbit.generate_coin_address({
                                                                                        'currency': 'BTC',
                                                                                    })
        self.assertTrue('error' not in json_data)

    def test_get_coin_address_list(self):
        json_data = Upbit.get_coin_address_list()
        self.assertTrue('error' not in json_data)

    def test_get_coin_address(self):
        json_data = Upbit.get_coin_address({
                                                                            'currency': 'BTC',
                                                                        })
        self.assertTrue('error' not in json_data)

    def test_deposit_krw(self):
        json_data = Upbit.deposit_krw({
                                                                    'amount': '10000',
                                                                })
        self.assertTrue('error' not in json_data)

    def test_get_status_wallet(self):
        json_data = Upbit.get_status_wallet()
        self.assertTrue('error' not in json_data)

    def test_get_api_key_list(self):
        json_data = Upbit.get_api_key_list()
        self.assertTrue('error' not in json_data)

    def test_get_market_info(self):
        json_data = Upbit.get_market_info()
        self.assertTrue('error' not in json_data)

    def test_get_candle_info(self):
        json_data = Upbit.get_candle_info('KRW-BTC', 'minutes/1')
        self.assertTrue('error' not in json_data)

    def test_get_trade_info_tick(self):
        json_data = Upbit.get_trade_info_tick('KRW-BTC')
        self.assertTrue('error' not in json_data)

    def test_get_market_info_ticker(self):
        json_data = Upbit.get_market_info_ticker(["KRW-BTC","KRW-EOS"])
        self.assertTrue('error' not in json_data)

    def test_get_orderbook(self):
        json_data = Upbit.get_orderbook(["KRW-BTC","KRW-EOS"])
        self.assertTrue('error' not in json_data)



if __name__ == '__main__':
    unittest.main()