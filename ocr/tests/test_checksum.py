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

