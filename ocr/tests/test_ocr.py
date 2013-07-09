from textwrap import dedent
from unittest import TestCase

from ocr.parser import parse_ocr


class OCRTest(TestCase):

    def test_zero(self):
        content = dedent("""\
             _  _  _  _  _  _  _  _  _ 
            | || || || || || || || || |
            |_||_||_||_||_||_||_||_||_|
            """)
        self.assertEqual('000000000', parse_ocr(content))

    def test_all(self):
        content = dedent("""\
              _     _  _     _  _  _  _  _ 
             | |  | _| _||_||_ |_   ||_||_|
             |_|  ||_  _|  | _||_|  ||_| _|
            """)
        self.assertEqual('0123456789', parse_ocr(content))

    def test_malformed(self):
        content = dedent("""\
                 _  _  _  _  _  _     _ 
             |_||_|| || ||_   |  |  | _ 
               | _||_||_||_|  |  |  | _|
            """)
        self.assertEqual('49006771?', parse_ocr(content))
        content = dedent("""\
                 _  _     _  _  _  _  _ 
             |_| _| _||_| _ |_   ||_||_|
               ||_  _|  | _||_|  ||_| _ 
            """)
        self.assertEqual('4234?678?', parse_ocr(content))
