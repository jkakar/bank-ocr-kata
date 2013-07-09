valid1 = """
 _  _  _  _  _  _  _  _    
| || || || || || || ||_   |
|_||_||_||_||_||_||_| _|  |
"""
                           
ill1 = """
    _  _  _  _  _  _     _ 
|_||_|| || ||_   |  |  | _ 
  | _||_||_||_|  |  |  | _|
"""
# ILL
                           
ill2 = """
    _  _     _  _  _  _  _ 
  | _| _||_| _ |_   ||_||_|
  ||_  _|  | _||_|  ||_| _ 
"""
#ILL

err1 = """
 _     _  _  _  _  _  _  _ 
 _||_||_ |_||_| _||_||_ |_ 
 _|  | _||_||_||_ |_||_| _|
"""
#ERR


directory = [valid1, ill1, ill2, err1]

from unittest import TestCase

from ocr.reporter import generate_report

class ReportGeneratorTest(TestCase):
    def test_generate_empty_report(self):
        self.assertEqual([], generate_report([]))

    def test_generate_valid_report(self):
        self.assertEqual([('', '000000051'),
                          ('ILL', '49006771?'),
                          ('ILL', '1234?678?'),
                          ('ERR', '345882865')], generate_report(directory))
