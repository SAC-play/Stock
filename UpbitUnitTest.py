import sys
sys.path.append('./Upbit')

import UpbitApi as Upbit
import unittest

class UpbitUnitTest(unittest.TestCase):
    def test_get_my_account_info(self):
        json_data = Upbit.get_my_account_info()
        self.assertTrue('error' in json_data)

if __name__ == '__main__':
    unittest.main()