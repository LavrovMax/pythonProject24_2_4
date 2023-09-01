import pytest

from app.calc import Calculator


class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_adding_success(self):
        assert self.calc.adding(self, 2, 1) == 3

    def test_subtraction_success(self):
        assert self.calc.subtraction(self, 5, 2) == 3

    def test_multiply_success(self):
        assert self.calc.multiply(self, 3, 3) == 9

    def test_division_success(self):
        assert self.calc.division(self, 9, 3) == 3

    def Test_zero_division(self):
        with pytest.raises(ZeroDivisionError):
            self.calc.division(1, 0)

    def teardoun(self):
        print('Выполнение метода teardoun')