"""
Calculator app tests
SPDX - License - Identifier: LGPL - 3.0 - or -later
Auteurs : Gabriel C. Ullmann, Fabio Petrillo, 2025
"""

from calculator import Calculator

def test_app():
    my_calculator = Calculator()
    assert my_calculator.get_hello_message() == "== Calculatrice v1.0 =="

# TODO: ajoutez les tests
import pytest
from calculator import Calculator

@pytest.fixture
def calc():
    return Calculator()

def test_get_hello_message(calc):
    assert calc.get_hello_message() == "== Calculatrice v1.0 =="

def test_addition(calc):
    assert calc.addition(2, 3) == 5
    assert calc.addition(-1, 1) == 0

def test_subtraction(calc):
    assert calc.subtraction(5, 3) == 2
    assert calc.subtraction(0, 4) == -4

def test_multiplication(calc):
    assert calc.multiplication(3, 4) == 12
    assert calc.multiplication(-2, 3) == -6

def test_division(calc):
    assert calc.division(10, 2) == 5
    assert calc.division(5, 0) == "Erreur : division par zéro"
from calculator import Calculator
import pytest

def test_addition_fail():
    calc = Calculator()
    # Ce test va échouer volontairement : 2 + 3 ≠ 6
    assert calc.addition(2, 3) == 6
