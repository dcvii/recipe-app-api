# sample tests

from django.test import SimpleTestCase
from app import calc

class CalcTest(SimpleTestCase):
    # test the add function

    def test_add(self):
        #test adding numbers together
        result = calc.add(3,8)
        self.assertEqual(result, 11)

    # test the subtract function
    def test_subtract(self):
        # test subtracting numbers together
        result = calc.subtract(5,11)
        self.assertEqual(result, 6)

        