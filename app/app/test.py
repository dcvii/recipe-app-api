from django.test import SimpleTestCase
from app import calc

class CalcTest(SimpleTestCase):


    # test adding numbers together
    def test_add(self):
        result = calc.add(3, 8)
        self.assertEqual(result, 11)

    # test the subtract function
    def test_subtract(self):
        result = calc.subtract(5, 11)
        self.assertEqual(result, 6)
