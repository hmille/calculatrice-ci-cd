from src import calculatrice

def test_addition():
    assert calculatrice.addition(2, 3) == 5

def test_soustraction():
    assert calculatrice.soustraction(5, 3) == 2

def test_multiplication():
    assert calculatrice.multiplication(2, 3) == 6

def test_division():
    assert calculatrice.division(10, 2) == 5

