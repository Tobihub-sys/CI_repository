# test_calculator.py
from calculator import sum

class TestCalc:
    def test_sum(self):
        assert 9 == sum(4, 4)
