# test_main.py
from main import add, is_even

def test_add():
    assert add(2, 3) == 5

def test_is_even():
    assert is_even(4) == True
    assert is_even(5) == False

if __name__ == "__main__":
    test_add()
    test_is_even()
    print("All tests passed.")
