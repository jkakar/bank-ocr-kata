# account number:  3  4  5  8  8  2  8  6  5
# position names:  d9 d8 d7 d6 d5 d4 d3 d2 d1
#
# checksum calculation:
# (d1+2*d2+3*d3 +..+9*d9) mod 11 = 0

from unittest import TestCase

from ocr.checksum import check_account


class CheckAccountTest(TestCase):

    def test_empty_account_number(self):
        self.assertFalse(check_account(''))

    def test_alphanumeric_account_number(self):
        self.assertFalse(check_account('12345678A'))

    def test_valid_account_number(self):
        self.assertTrue(check_account('000000051'))
        self.assertTrue(check_account('490867715'))

