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

if __name__ == '__main__':
    unittest.main()