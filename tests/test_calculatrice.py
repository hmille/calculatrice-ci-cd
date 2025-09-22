import pytest
import sys
import os

# Ajouter src/ au path Python
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

import calculatrice

def test_addition():
    assert calculatrice.addition(2, 3) == 5

def test_soustraction():
    assert calculatrice.soustraction(10, 4) == 6

def test_multiplication():
    assert calculatrice.multiplication(3, 7) == 21

def test_division():
    assert calculatrice.division(8, 2) == 4

def test_division_par_zero():
    with pytest.raises(ValueError):
        calculatrice.division(5, 0)
